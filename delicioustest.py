import delicious
import unittest
import sys

class APIMethods(unittest.TestCase):
  api_methods = (
    'last_update',
    'add',
    'delete',
    'bookmark',
    'dates',
    'bookmarks',
    'recent',
    'suggest',
    'all_tags',
    'delete_tag',
    'rename_tag',
    'all_tag_bundles',
    'set_tag_bundle',
    'delete_tag_bundle'
  )
  
  def test_api_methods(self):
    '''account should provide access to all known API calls'''
    account = delicious.Account('dummy', 'pass')
    for method in self.api_methods:
      self.assertIn(method, dir(account))

if __name__ == '__main__':
  unittest.main()