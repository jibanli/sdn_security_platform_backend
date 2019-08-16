from django.test import TestCase
from sdn_communication.tasks import get_switch_number, get_switch_desc, get_flow_stats, get_agg_flow_stats, get_port_stats
from sdn_communication.tasks import write_switch_desc, write_flow_stats
from sdn_communication.models import Switch, DescStats, FlowStats, FlowAggregateStats, TableStats, PortStats 
from rest_framework import status
from requests.models import Response

class TasksTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):

        #Description hardware response
        cls.flow_stats_response = Response()
        cls.flow_stats_response.status_code = 200
        cls.flow_stats_response._content = b'{ "1" : [{ \
            "actions"       : ["OUTPUT:2"],     \
            "idle_timeout"  : "0",              \
            "cookie"        : "0",              \
            "packet_count"  : "0",              \
            "hard_timeout"  : "0",              \
            "byte_count"    : "728",            \
            "duration_sec"  : "35",             \
            "duration_nsec" : "126000000",      \
            "priority"      : "1",              \
            "length"        : "104",            \
            "flags"         : "0",              \
            "table_id"      : "0",              \
            "match" : {                         \
                "dl_dest" : "00:00:00:00:00:00", \
                "dl_src"  : "00:00:00:00:00:00", \
                "in_port" : "3" }, \
            "serial_num" : "1234" }]}'
        
        #Description hardware response
        cls.switch_desc_response = Response()
        cls.switch_desc_response.status_code = 200
        cls.switch_desc_response._content = b'{ "1" : {"dp_desc" : "None",\
            "mfr_desc"   : "2.9.2",         \
            "hw_desc"    : "Open VSwitch",  \
            "sw_desc"    : "None",          \
            "serial_num" : "Nicira, Inc." }}'


    def test_write_switch_desc(self):
        """Writing the hardware description"""
        #switch_desc = DescStats.objects.get(dp_desc = "Apple")
        self.assertEqual(write_switch_desc(self.switch_desc_response), True)

    def test_write_flow_stats(self):
        self.assertEqual(write_flow_stats(self.flow_stats_response), True)