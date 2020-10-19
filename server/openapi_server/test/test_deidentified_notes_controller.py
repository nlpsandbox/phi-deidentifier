# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDeidentifiedNotesController(BaseTestCase):
    """DeidentifiedNotesController integration test stubs"""

    def test_deidentified_notes_read_all(self):
        """Test case for deidentified_notes_read_all

        Get deidentified notes
        """
        note = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/deidentified-notes',
            method='GET',
            headers=headers,
            data=json.dumps(note),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
