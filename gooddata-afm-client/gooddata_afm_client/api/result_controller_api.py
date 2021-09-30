"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gooddata_afm_client.api_client import ApiClient, Endpoint as _Endpoint
from gooddata_afm_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gooddata_afm_client.model.error_message import ErrorMessage
from gooddata_afm_client.model.execution_result import ExecutionResult


class ResultControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __retrieve_result(
            self,
            workspace_id,
            result_id,
            **kwargs
        ):
            """Get a single execution result  # noqa: E501

            Gets a single execution result.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.retrieve_result(workspace_id, result_id, async_req=True)
            >>> result = thread.get()

            Args:
                workspace_id (str): Workspace identifier
                result_id (str): Result ID

            Keyword Args:
                offset ([int]): Request page with these offsets. Format is offset=1,2,3,... - one offset for each dimensions in ResultSpec from originating AFM.. [optional] if omitted the server will use the default value of []
                limit ([int]): Return only this number of items. Format is limit=1,2,3,... - one limit for each dimensions in ResultSpec from originating AFM.. [optional] if omitted the server will use the default value of []
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ExecutionResult
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['workspace_id'] = \
                workspace_id
            kwargs['result_id'] = \
                result_id
            return self.call_with_http_info(**kwargs)

        self.retrieve_result = _Endpoint(
            settings={
                'response_type': (ExecutionResult,),
                'auth': [],
                'endpoint_path': '/api/actions/workspaces/{workspaceId}/execution/afm/execute/result/{resultId}',
                'operation_id': 'retrieve_result',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'result_id',
                    'offset',
                    'limit',
                ],
                'required': [
                    'workspace_id',
                    'result_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'workspace_id',
                ]
            },
            root_map={
                'validations': {
                    ('workspace_id',): {

                        'regex': {
                            'pattern': r'^[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'result_id':
                        (str,),
                    'offset':
                        ([int],),
                    'limit':
                        ([int],),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'result_id': 'resultId',
                    'offset': 'offset',
                    'limit': 'limit',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'result_id': 'path',
                    'offset': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                    'offset': 'csv',
                    'limit': 'csv',
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__retrieve_result
        )