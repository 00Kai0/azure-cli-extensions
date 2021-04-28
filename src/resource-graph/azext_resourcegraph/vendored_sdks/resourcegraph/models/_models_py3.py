# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._resource_graph_client_enums import *


class Column(msrest.serialization.Model):
    """Query result column descriptor.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Column name.
    :type name: str
    :param type: Required. Column data type. Possible values include: "string", "integer",
     "number", "boolean", "object".
    :type type: str or ~azure.mgmt.resourcegraph.models.ColumnDataType
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        type: Union[str, "ColumnDataType"],
        **kwargs
    ):
        super(Column, self).__init__(**kwargs)
        self.name = name
        self.type = type


class Error(msrest.serialization.Model):
    """Error details.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Error code identifying the specific error.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param details: Error details.
    :type details: list[~azure.mgmt.resourcegraph.models.ErrorDetails]
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetails]'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        details: Optional[List["ErrorDetails"]] = None,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = details


class ErrorDetails(msrest.serialization.Model):
    """Error details.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param code: Required. Error code identifying the specific error.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        additional_properties: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(ErrorDetails, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message


class ErrorFieldContract(msrest.serialization.Model):
    """Error Field contract.

    :param code: Property level error code.
    :type code: str
    :param message: Human-readable representation of property-level error.
    :type message: str
    :param target: Property name.
    :type target: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        **kwargs
    ):
        super(ErrorFieldContract, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target


class ErrorResponse(msrest.serialization.Model):
    """An error response from the API.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. Error information.
    :type error: ~azure.mgmt.resourcegraph.models.Error
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(
        self,
        *,
        error: "Error",
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class Facet(msrest.serialization.Model):
    """A facet containing additional statistics on the response of a query. Can be either FacetResult or FacetError.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: FacetError, FacetResult.

    All required parameters must be populated in order to send to Azure.

    :param expression: Required. Facet expression, same as in the corresponding facet request.
    :type expression: str
    :param result_type: Required. Result type.Constant filled by server.
    :type result_type: str
    """

    _validation = {
        'expression': {'required': True},
        'result_type': {'required': True},
    }

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
    }

    _subtype_map = {
        'result_type': {'FacetError': 'FacetError', 'FacetResult': 'FacetResult'}
    }

    def __init__(
        self,
        *,
        expression: str,
        **kwargs
    ):
        super(Facet, self).__init__(**kwargs)
        self.expression = expression
        self.result_type = None  # type: Optional[str]


class FacetError(Facet):
    """A facet whose execution resulted in an error.

    All required parameters must be populated in order to send to Azure.

    :param expression: Required. Facet expression, same as in the corresponding facet request.
    :type expression: str
    :param result_type: Required. Result type.Constant filled by server.
    :type result_type: str
    :param errors: Required. An array containing detected facet errors with details.
    :type errors: list[~azure.mgmt.resourcegraph.models.ErrorDetails]
    """

    _validation = {
        'expression': {'required': True},
        'result_type': {'required': True},
        'errors': {'required': True},
    }

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'errors': {'key': 'errors', 'type': '[ErrorDetails]'},
    }

    def __init__(
        self,
        *,
        expression: str,
        errors: List["ErrorDetails"],
        **kwargs
    ):
        super(FacetError, self).__init__(expression=expression, **kwargs)
        self.result_type = 'FacetError'  # type: str
        self.errors = errors


class FacetRequest(msrest.serialization.Model):
    """A request to compute additional statistics (facets) over the query results.

    All required parameters must be populated in order to send to Azure.

    :param expression: Required. The column or list of columns to summarize by.
    :type expression: str
    :param options: The options for facet evaluation.
    :type options: ~azure.mgmt.resourcegraph.models.FacetRequestOptions
    """

    _validation = {
        'expression': {'required': True},
    }

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'options': {'key': 'options', 'type': 'FacetRequestOptions'},
    }

    def __init__(
        self,
        *,
        expression: str,
        options: Optional["FacetRequestOptions"] = None,
        **kwargs
    ):
        super(FacetRequest, self).__init__(**kwargs)
        self.expression = expression
        self.options = options


class FacetRequestOptions(msrest.serialization.Model):
    """The options for facet evaluation.

    :param sort_by: The column name or query expression to sort on. Defaults to count if not
     present.
    :type sort_by: str
    :param sort_order: The sorting order by the selected column (count by default). Possible values
     include: "asc", "desc". Default value: "desc".
    :type sort_order: str or ~azure.mgmt.resourcegraph.models.FacetSortOrder
    :param filter: Specifies the filter condition for the 'where' clause which will be run on main
     query's result, just before the actual faceting.
    :type filter: str
    :param top: The maximum number of facet rows that should be returned.
    :type top: int
    """

    _validation = {
        'top': {'maximum': 1000, 'minimum': 1},
    }

    _attribute_map = {
        'sort_by': {'key': 'sortBy', 'type': 'str'},
        'sort_order': {'key': 'sortOrder', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'str'},
        'top': {'key': '$top', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        sort_by: Optional[str] = None,
        sort_order: Optional[Union[str, "FacetSortOrder"]] = "desc",
        filter: Optional[str] = None,
        top: Optional[int] = None,
        **kwargs
    ):
        super(FacetRequestOptions, self).__init__(**kwargs)
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.filter = filter
        self.top = top


class FacetResult(Facet):
    """Successfully executed facet containing additional statistics on the response of a query.

    All required parameters must be populated in order to send to Azure.

    :param expression: Required. Facet expression, same as in the corresponding facet request.
    :type expression: str
    :param result_type: Required. Result type.Constant filled by server.
    :type result_type: str
    :param total_records: Required. Number of total records in the facet results.
    :type total_records: long
    :param count: Required. Number of records returned in the facet response.
    :type count: int
    :param data: Required. A table containing the desired facets. Only present if the facet is
     valid.
    :type data: object
    """

    _validation = {
        'expression': {'required': True},
        'result_type': {'required': True},
        'total_records': {'required': True},
        'count': {'required': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'total_records': {'key': 'totalRecords', 'type': 'long'},
        'count': {'key': 'count', 'type': 'int'},
        'data': {'key': 'data', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        expression: str,
        total_records: int,
        count: int,
        data: object,
        **kwargs
    ):
        super(FacetResult, self).__init__(expression=expression, **kwargs)
        self.result_type = 'FacetResult'  # type: str
        self.total_records = total_records
        self.count = count
        self.data = data


class GraphQueryError(msrest.serialization.Model):
    """Error message body that will indicate why the operation failed.

    :param code: Service-defined error code. This code serves as a sub-status for the HTTP error
     code specified in the response.
    :type code: str
    :param message: Human-readable representation of the error.
    :type message: str
    :param details: The list of invalid fields send in request, in case of validation error.
    :type details: list[~azure.mgmt.resourcegraph.models.ErrorFieldContract]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorFieldContract]'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        details: Optional[List["ErrorFieldContract"]] = None,
        **kwargs
    ):
        super(GraphQueryError, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = details


class GraphQueryListResult(msrest.serialization.Model):
    """Graph query list result.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param next_link: URL to fetch the next set of queries.
    :type next_link: str
    :ivar value: An array of graph queries.
    :vartype value: list[~azure.mgmt.resourcegraph.models.GraphQueryResource]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[GraphQueryResource]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(GraphQueryListResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = None


class Resource(msrest.serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name. This is GUID value. The display name should be assigned within
     properties field.
    :vartype name: str
    :param location: The location of the resource.
    :type location: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param etag: This will be used to handle Optimistic Concurrency. If not present, it will always
     overwrite the existing resource without checking conflict.
    :type etag: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        etag: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.location = location
        self.type = None
        self.etag = etag
        self.tags = tags


class GraphQueryResource(Resource):
    """Graph Query entity definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name. This is GUID value. The display name should be assigned within
     properties field.
    :vartype name: str
    :param location: The location of the resource.
    :type location: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param etag: This will be used to handle Optimistic Concurrency. If not present, it will always
     overwrite the existing resource without checking conflict.
    :type etag: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :ivar time_modified: Date and time in UTC of the last modification that was made to this graph
     query definition.
    :vartype time_modified: ~datetime.datetime
    :param description: The description of a graph query.
    :type description: str
    :param query: KQL query that will be graph.
    :type query: str
    :ivar result_kind: Enum indicating a type of graph query. Possible values include: "basic".
    :vartype result_kind: str or ~azure.mgmt.resourcegraph.models.ResultKind
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'time_modified': {'readonly': True},
        'result_kind': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'time_modified': {'key': 'properties.timeModified', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'query': {'key': 'properties.query', 'type': 'str'},
        'result_kind': {'key': 'properties.resultKind', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        etag: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        query: Optional[str] = None,
        **kwargs
    ):
        super(GraphQueryResource, self).__init__(location=location, etag=etag, tags=tags, **kwargs)
        self.time_modified = None
        self.description = description
        self.query = query
        self.result_kind = None


class GraphQueryUpdateParameters(msrest.serialization.Model):
    """The parameters that can be provided when updating workbook properties properties.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param etag: This will be used to handle Optimistic Concurrency. If not present, it will always
     overwrite the existing resource without checking conflict.
    :type etag: str
    :param description: The description of a graph query.
    :type description: str
    :param query: KQL query that will be graph.
    :type query: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'query': {'key': 'properties.query', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        etag: Optional[str] = None,
        description: Optional[str] = None,
        query: Optional[str] = None,
        **kwargs
    ):
        super(GraphQueryUpdateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.etag = etag
        self.description = description
        self.query = query


class Operation(msrest.serialization.Model):
    """Resource Graph REST API operation definition.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display: ~azure.mgmt.resourcegraph.models.OperationDisplay
    :param origin: The origin of operations.
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        origin: Optional[str] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin


class OperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :param provider: Service provider: Microsoft Resource Graph.
    :type provider: str
    :param resource: Resource on which the operation is performed etc.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description for the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Resource Graph operations. It contains a list of operations and a URL link to get the next set of results.

    :param value: List of Resource Graph operations supported by the Resource Graph resource
     provider.
    :type value: list[~azure.mgmt.resourcegraph.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value


class QueryRequest(msrest.serialization.Model):
    """Describes a query to be executed.

    All required parameters must be populated in order to send to Azure.

    :param subscriptions: Required. Azure subscriptions against which to execute the query.
    :type subscriptions: list[str]
    :param query: Required. The resources query.
    :type query: str
    :param options: The query evaluation options.
    :type options: ~azure.mgmt.resourcegraph.models.QueryRequestOptions
    :param facets: An array of facet requests to be computed against the query result.
    :type facets: list[~azure.mgmt.resourcegraph.models.FacetRequest]
    """

    _validation = {
        'subscriptions': {'required': True},
        'query': {'required': True},
    }

    _attribute_map = {
        'subscriptions': {'key': 'subscriptions', 'type': '[str]'},
        'query': {'key': 'query', 'type': 'str'},
        'options': {'key': 'options', 'type': 'QueryRequestOptions'},
        'facets': {'key': 'facets', 'type': '[FacetRequest]'},
    }

    def __init__(
        self,
        *,
        subscriptions: List[str],
        query: str,
        options: Optional["QueryRequestOptions"] = None,
        facets: Optional[List["FacetRequest"]] = None,
        **kwargs
    ):
        super(QueryRequest, self).__init__(**kwargs)
        self.subscriptions = subscriptions
        self.query = query
        self.options = options
        self.facets = facets


class QueryRequestOptions(msrest.serialization.Model):
    """The options for query evaluation.

    :param skip_token: Continuation token for pagination, capturing the next page size and offset,
     as well as the context of the query.
    :type skip_token: str
    :param top: The maximum number of rows that the query should return. Overrides the page size
     when ``$skipToken`` property is present.
    :type top: int
    :param skip: The number of rows to skip from the beginning of the results. Overrides the next
     page offset when ``$skipToken`` property is present.
    :type skip: int
    :param result_format: Defines in which format query result returned. Possible values include:
     "table", "objectArray".
    :type result_format: str or ~azure.mgmt.resourcegraph.models.ResultFormat
    """

    _validation = {
        'top': {'maximum': 1000, 'minimum': 1},
        'skip': {'minimum': 0},
    }

    _attribute_map = {
        'skip_token': {'key': '$skipToken', 'type': 'str'},
        'top': {'key': '$top', 'type': 'int'},
        'skip': {'key': '$skip', 'type': 'int'},
        'result_format': {'key': 'resultFormat', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        skip_token: Optional[str] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        result_format: Optional[Union[str, "ResultFormat"]] = None,
        **kwargs
    ):
        super(QueryRequestOptions, self).__init__(**kwargs)
        self.skip_token = skip_token
        self.top = top
        self.skip = skip
        self.result_format = result_format


class QueryResponse(msrest.serialization.Model):
    """Query result.

    All required parameters must be populated in order to send to Azure.

    :param total_records: Required. Number of total records matching the query.
    :type total_records: long
    :param count: Required. Number of records returned in the current response. In the case of
     paging, this is the number of records in the current page.
    :type count: long
    :param result_truncated: Required. Indicates whether the query results are truncated. Possible
     values include: "true", "false".
    :type result_truncated: str or ~azure.mgmt.resourcegraph.models.ResultTruncated
    :param skip_token: When present, the value can be passed to a subsequent query call (together
     with the same query and subscriptions used in the current request) to retrieve the next page of
     data.
    :type skip_token: str
    :param data: Required. Query output in tabular format.
    :type data: object
    :param facets: Query facets.
    :type facets: list[~azure.mgmt.resourcegraph.models.Facet]
    """

    _validation = {
        'total_records': {'required': True},
        'count': {'required': True},
        'result_truncated': {'required': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'total_records': {'key': 'totalRecords', 'type': 'long'},
        'count': {'key': 'count', 'type': 'long'},
        'result_truncated': {'key': 'resultTruncated', 'type': 'str'},
        'skip_token': {'key': '$skipToken', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'facets': {'key': 'facets', 'type': '[Facet]'},
    }

    def __init__(
        self,
        *,
        total_records: int,
        count: int,
        result_truncated: Union[str, "ResultTruncated"],
        data: object,
        skip_token: Optional[str] = None,
        facets: Optional[List["Facet"]] = None,
        **kwargs
    ):
        super(QueryResponse, self).__init__(**kwargs)
        self.total_records = total_records
        self.count = count
        self.result_truncated = result_truncated
        self.skip_token = skip_token
        self.data = data
        self.facets = facets


class Table(msrest.serialization.Model):
    """Query output in tabular format.

    All required parameters must be populated in order to send to Azure.

    :param columns: Required. Query result column descriptors.
    :type columns: list[~azure.mgmt.resourcegraph.models.Column]
    :param rows: Required. Query result rows.
    :type rows: list[list[object]]
    """

    _validation = {
        'columns': {'required': True},
        'rows': {'required': True},
    }

    _attribute_map = {
        'columns': {'key': 'columns', 'type': '[Column]'},
        'rows': {'key': 'rows', 'type': '[[object]]'},
    }

    def __init__(
        self,
        *,
        columns: List["Column"],
        rows: List[List[object]],
        **kwargs
    ):
        super(Table, self).__init__(**kwargs)
        self.columns = columns
        self.rows = rows
