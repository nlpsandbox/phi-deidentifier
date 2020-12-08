# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.text_annotation import TextAnnotation
from openapi_server.models.text_physical_address_annotation_all_of import TextPhysicalAddressAnnotationAllOf
from openapi_server import util

from openapi_server.models.text_annotation import TextAnnotation  # noqa: E501
from openapi_server.models.text_physical_address_annotation_all_of import TextPhysicalAddressAnnotationAllOf  # noqa: E501

class TextPhysicalAddressAnnotation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start=None, length=None, text=None, address_type=None):  # noqa: E501
        """TextPhysicalAddressAnnotation - a model defined in OpenAPI

        :param start: The start of this TextPhysicalAddressAnnotation.  # noqa: E501
        :type start: int
        :param length: The length of this TextPhysicalAddressAnnotation.  # noqa: E501
        :type length: int
        :param text: The text of this TextPhysicalAddressAnnotation.  # noqa: E501
        :type text: str
        :param address_type: The address_type of this TextPhysicalAddressAnnotation.  # noqa: E501
        :type address_type: str
        """
        self.openapi_types = {
            'start': int,
            'length': int,
            'text': str,
            'address_type': str
        }

        self.attribute_map = {
            'start': 'start',
            'length': 'length',
            'text': 'text',
            'address_type': 'addressType'
        }

        self._start = start
        self._length = length
        self._text = text
        self._address_type = address_type

    @classmethod
    def from_dict(cls, dikt) -> 'TextPhysicalAddressAnnotation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextPhysicalAddressAnnotation of this TextPhysicalAddressAnnotation.  # noqa: E501
        :rtype: TextPhysicalAddressAnnotation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self):
        """Gets the start of this TextPhysicalAddressAnnotation.

        The position of the first character  # noqa: E501

        :return: The start of this TextPhysicalAddressAnnotation.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TextPhysicalAddressAnnotation.

        The position of the first character  # noqa: E501

        :param start: The start of this TextPhysicalAddressAnnotation.
        :type start: int
        """

        self._start = start

    @property
    def length(self):
        """Gets the length of this TextPhysicalAddressAnnotation.

        The length of the annotation  # noqa: E501

        :return: The length of this TextPhysicalAddressAnnotation.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this TextPhysicalAddressAnnotation.

        The length of the annotation  # noqa: E501

        :param length: The length of this TextPhysicalAddressAnnotation.
        :type length: int
        """

        self._length = length

    @property
    def text(self):
        """Gets the text of this TextPhysicalAddressAnnotation.

        The string annotated  # noqa: E501

        :return: The text of this TextPhysicalAddressAnnotation.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextPhysicalAddressAnnotation.

        The string annotated  # noqa: E501

        :param text: The text of this TextPhysicalAddressAnnotation.
        :type text: str
        """

        self._text = text

    @property
    def address_type(self):
        """Gets the address_type of this TextPhysicalAddressAnnotation.

        Type of address information  # noqa: E501

        :return: The address_type of this TextPhysicalAddressAnnotation.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this TextPhysicalAddressAnnotation.

        Type of address information  # noqa: E501

        :param address_type: The address_type of this TextPhysicalAddressAnnotation.
        :type address_type: str
        """
        allowed_values = ["city", "country", "department", "hospital", "organization", "other", "room", "state", "street", "zip"]  # noqa: E501
        if address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `address_type` ({0}), must be one of {1}"
                .format(address_type, allowed_values)
            )

        self._address_type = address_type