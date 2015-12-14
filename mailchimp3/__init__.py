"""
Mailchimp v3 Api SDK

"""
from mailchimp3.mailchimpclient import MailChimpClient
from mailchimp3.entities.authorizedapp import AuthorizedApp
from mailchimp3.entities.automation import Automation
from mailchimp3.entities.message import Message
from mailchimp3.entities.campaign import Campaign
from mailchimp3.entities.report import Report
from mailchimp3.entities.feedback import Feedback
from mailchimp3.entities.conversation import Conversation
from mailchimp3.entities.listabuse import ListAbuse
from mailchimp3.entities.listactivity import ListActivity
from mailchimp3.entities.memberactivity import MemberActivity
from mailchimp3.entities.reportactivity import ReportActivity
from mailchimp3.entities.client import Client
from mailchimp3.entities.list import List
from mailchimp3.entities.growth import Growth
from mailchimp3.entities.template import Template
from mailchimp3.entities.interest import Interest
from mailchimp3.entities.category import Category
from mailchimp3.entities.goal import Goal
from mailchimp3.entities.member import Member
from mailchimp3.entities.reportabuse import ReportAbuse
from mailchimp3.entities.files import File
from mailchimp3.entities.automationemail import AutomationEmail
from mailchimp3.entities.automationemailqueue import AutomationEmailQueue
from mailchimp3.entities.automationeremovedsubscriber import AutomationRemovedSubscriber


class MailChimp(MailChimpClient):
    """
    MailChimp class to communicate with the v3 API
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the class with your user_id and secret_key
        """
        super(MailChimp, self).__init__(*args, **kwargs)
        # Authorized Apps
        self.authorized_app = AuthorizedApp(self)
        # Automation
        self.automation = Automation(self)
        self.automationemail = AutomationEmail(self)
        self.automationemailqueue = AutomationEmailQueue(self)
        self.automationeremovedsubscriber = AutomationRemovedSubscriber(self)
        # Campaigns
        self.campaign = Campaign(self)
        self.report = Report(self)
        self.campaignfeedback = Feedback(self)
        self.conversation = Conversation(self)
        self.message = Message(self)
        self.listactivity = ListActivity(self)
        self.listabuse = ListAbuse(self)
        self.client = Client(self)
        self.list = List(self)
        self.growth = Growth(self)
        self.template = Template(self)
        self.file = File(self)
        self.category = Category(self)
        self.interest = Interest(self)
        self.memberactivity = MemberActivity(self)
        self.reportactivity = ReportActivity(self)
        self.goal = Goal(self)
        self.member = Member(self)
        self.reportabuse = ReportAbuse(self)
