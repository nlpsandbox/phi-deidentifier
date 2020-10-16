# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.entity import Entity
from openapi_server.models.user import User
from openapi_server import util

from openapi_server.models.entity import Entity  # noqa: E501
from openapi_server.models.user import User  # noqa: E501

class Note(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text=None, patient_public_id=None, type=None, id=None, created_by=None, created_at=None, updated_by=None, updated_at=None):  # noqa: E501
        """Note - a model defined in OpenAPI

        :param text: The text of this Note.  # noqa: E501
        :type text: str
        :param patient_public_id: The patient_public_id of this Note.  # noqa: E501
        :type patient_public_id: str
        :param type: The type of this Note.  # noqa: E501
        :type type: str
        :param id: The id of this Note.  # noqa: E501
        :type id: int
        :param created_by: The created_by of this Note.  # noqa: E501
        :type created_by: User
        :param created_at: The created_at of this Note.  # noqa: E501
        :type created_at: datetime
        :param updated_by: The updated_by of this Note.  # noqa: E501
        :type updated_by: User
        :param updated_at: The updated_at of this Note.  # noqa: E501
        :type updated_at: datetime
        """
        self.openapi_types = {
            'text': str,
            'patient_public_id': str,
            'type': str,
            'id': int,
            'created_by': User,
            'created_at': datetime,
            'updated_by': User,
            'updated_at': datetime
        }

        self.attribute_map = {
            'text': 'text',
            'patient_public_id': 'patientPublicId',
            'type': 'type',
            'id': 'id',
            'created_by': 'createdBy',
            'created_at': 'createdAt',
            'updated_by': 'updatedBy',
            'updated_at': 'updatedAt'
        }

        self._text = text
        self._patient_public_id = patient_public_id
        self._type = type
        self._id = id
        self._created_by = created_by
        self._created_at = created_at
        self._updated_by = updated_by
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'Note':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Note of this Note.  # noqa: E501
        :rtype: Note
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self):
        """Gets the text of this Note.

        The content of the note  # noqa: E501

        :return: The text of this Note.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Note.

        The content of the note  # noqa: E501

        :param text: The text of this Note.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def patient_public_id(self):
        """Gets the patient_public_id of this Note.


        :return: The patient_public_id of this Note.
        :rtype: str
        """
        return self._patient_public_id

    @patient_public_id.setter
    def patient_public_id(self, patient_public_id):
        """Sets the patient_public_id of this Note.


        :param patient_public_id: The patient_public_id of this Note.
        :type patient_public_id: str
        """

        self._patient_public_id = patient_public_id

    @property
    def type(self):
        """Gets the type of this Note.

        The note type  # noqa: E501

        :return: The type of this Note.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Note.

        The note type  # noqa: E501

        :param type: The type of this Note.
        :type type: str
        """
        allowed_values = ["pathology", "phone_call"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """Gets the id of this Note.

        ID  # noqa: E501

        :return: The id of this Note.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Note.

        ID  # noqa: E501

        :param id: The id of this Note.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this Note.


        :return: The created_by of this Note.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Note.


        :param created_by: The created_by of this Note.
        :type created_by: User
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this Note.

        When the entity has been created  # noqa: E501

        :return: The created_at of this Note.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Note.

        When the entity has been created  # noqa: E501

        :param created_at: The created_at of this Note.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_by(self):
        """Gets the updated_by of this Note.


        :return: The updated_by of this Note.
        :rtype: User
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Note.


        :param updated_by: The updated_by of this Note.
        :type updated_by: User
        """

        self._updated_by = updated_by

    @property
    def updated_at(self):
        """Gets the updated_at of this Note.

        When the entity has been updated  # noqa: E501

        :return: The updated_at of this Note.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Note.

        When the entity has been updated  # noqa: E501

        :param updated_at: The updated_at of this Note.
        :type updated_at: datetime
        """

        self._updated_at = updated_at