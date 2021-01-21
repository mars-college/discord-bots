import os
import pytz
import datetime
from dotenv import load_dotenv
from easydict import EasyDict
from gcsa.google_calendar import GoogleCalendar


calendar = None
calendar_settings = None
already_notified = {}  # maybe this might grow too big?        


def setup(calendar_settings_):
    global calendar, calendar_settings
    calendar_settings = calendar_settings_
    load_dotenv()
    calendar_id = os.getenv('CALENDAR_ID')
    calendar_credentials = os.getenv('CALENDAR_CREDENTIALS_FILE')
    calendar = GoogleCalendar(calendar_id, credentials_path=calendar_credentials)


def get_upcoming_events():
    time_before = calendar_settings.minutes_before * 60  # how long before event to notify
    check_every = calendar_settings.check_every * 60     # how often to check for events in loop

    # check events from now for the next 24 hours
    current_time = datetime.datetime.now(pytz.timezone('US/Pacific'))
    end_time = current_time + datetime.timedelta(days=1)

    # get events from calendar
    events = calendar.get_events(current_time, end_time, order_by='updated', single_events=True)
    events = [EasyDict({'event': event, 
                        'time': event.start, 
                        'time_until': event.start-current_time}) 
              for event in events]

    # filter events
    upcoming_events = [event for event in sorted(events, key=lambda k: k.time)  
        if event.event.id not in already_notified 
        and 0 <= event.time_until.total_seconds() <= (time_before + check_every)]

    return upcoming_events


def run(settings, data):
    include_description = settings.include_description
    response  = ':alarm_clock:  Event reminder!  :alarm_clock: \n'
    response += '**{}**\n'.format(data.summary)
    response += '**Location**: {}\n'.format(data.location)
    response += '**Time**: {} to {}'.format(data.start.strftime("%-I:%M %p"), data.end.strftime("%-I:%M %p"))
    if data.description and include_description:
        response += '\n\n{}'.format(data.description)
    already_notified[data.id] = True
    return response
