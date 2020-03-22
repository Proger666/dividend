from dividend.parsers.parse_table import ParseTable
from dividend.async_requests import AsyncRequests

class Screener:
  def __init__(self, table='dividend-growth', **filters):
    self.table = table
    self._scrape_table_func = ParseTable().parsers(table)
    self.page = 1
    self.total_records = 0
    self._filters = filters
    #print(self._filters)
    #response["last_price"] = 15
    #print(response)
    #print(self._scrape_table_func(response))
    self.data = self._search_screener()


  def _payload(self):
    default = {
      "tm":"3-screener",
      "r":"Webpage#1350",
      "only":["meta","data"],
      "tab": self.table,
      "page": self.page
    }
    for key, value in self._filters.items():
      default[key] = value
    return default

  def _search_screener(self):
    async_connector = AsyncRequests(self._payload(), self._scrape_table_func)
    async_connector_responses = async_connector.run()
    self.total_records = async_connector._total_records
    
    return async_connector_responses

  @classmethod
  def test(cls):
    return 'Hello World'