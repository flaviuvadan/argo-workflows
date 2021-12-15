"""
    Argo Server API

    You can get examples of requests and responses by using the CLI with `--gloglevel=9`, e.g. `argo list --gloglevel=9`  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from argo_workflows.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from argo_workflows.exceptions import ApiAttributeError


def lazy_import():
    from argo_workflows.model.io_argoproj_events_v1alpha1_amqp_event_source import IoArgoprojEventsV1alpha1AMQPEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_azure_events_hub_event_source import IoArgoprojEventsV1alpha1AzureEventsHubEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_bitbucket_server_event_source import IoArgoprojEventsV1alpha1BitbucketServerEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_calendar_event_source import IoArgoprojEventsV1alpha1CalendarEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_emitter_event_source import IoArgoprojEventsV1alpha1EmitterEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_file_event_source import IoArgoprojEventsV1alpha1FileEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_generic_event_source import IoArgoprojEventsV1alpha1GenericEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_github_event_source import IoArgoprojEventsV1alpha1GithubEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_gitlab_event_source import IoArgoprojEventsV1alpha1GitlabEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_hdfs_event_source import IoArgoprojEventsV1alpha1HDFSEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_kafka_event_source import IoArgoprojEventsV1alpha1KafkaEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_mqtt_event_source import IoArgoprojEventsV1alpha1MQTTEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_nats_events_source import IoArgoprojEventsV1alpha1NATSEventsSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_nsq_event_source import IoArgoprojEventsV1alpha1NSQEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_pub_sub_event_source import IoArgoprojEventsV1alpha1PubSubEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_pulsar_event_source import IoArgoprojEventsV1alpha1PulsarEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_redis_event_source import IoArgoprojEventsV1alpha1RedisEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_resource_event_source import IoArgoprojEventsV1alpha1ResourceEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_s3_artifact import IoArgoprojEventsV1alpha1S3Artifact
    from argo_workflows.model.io_argoproj_events_v1alpha1_service import IoArgoprojEventsV1alpha1Service
    from argo_workflows.model.io_argoproj_events_v1alpha1_slack_event_source import IoArgoprojEventsV1alpha1SlackEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_sns_event_source import IoArgoprojEventsV1alpha1SNSEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_sqs_event_source import IoArgoprojEventsV1alpha1SQSEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_storage_grid_event_source import IoArgoprojEventsV1alpha1StorageGridEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_stripe_event_source import IoArgoprojEventsV1alpha1StripeEventSource
    from argo_workflows.model.io_argoproj_events_v1alpha1_template import IoArgoprojEventsV1alpha1Template
    from argo_workflows.model.io_argoproj_events_v1alpha1_webhook_context import IoArgoprojEventsV1alpha1WebhookContext
    globals()['IoArgoprojEventsV1alpha1AMQPEventSource'] = IoArgoprojEventsV1alpha1AMQPEventSource
    globals()['IoArgoprojEventsV1alpha1AzureEventsHubEventSource'] = IoArgoprojEventsV1alpha1AzureEventsHubEventSource
    globals()['IoArgoprojEventsV1alpha1BitbucketServerEventSource'] = IoArgoprojEventsV1alpha1BitbucketServerEventSource
    globals()['IoArgoprojEventsV1alpha1CalendarEventSource'] = IoArgoprojEventsV1alpha1CalendarEventSource
    globals()['IoArgoprojEventsV1alpha1EmitterEventSource'] = IoArgoprojEventsV1alpha1EmitterEventSource
    globals()['IoArgoprojEventsV1alpha1FileEventSource'] = IoArgoprojEventsV1alpha1FileEventSource
    globals()['IoArgoprojEventsV1alpha1GenericEventSource'] = IoArgoprojEventsV1alpha1GenericEventSource
    globals()['IoArgoprojEventsV1alpha1GithubEventSource'] = IoArgoprojEventsV1alpha1GithubEventSource
    globals()['IoArgoprojEventsV1alpha1GitlabEventSource'] = IoArgoprojEventsV1alpha1GitlabEventSource
    globals()['IoArgoprojEventsV1alpha1HDFSEventSource'] = IoArgoprojEventsV1alpha1HDFSEventSource
    globals()['IoArgoprojEventsV1alpha1KafkaEventSource'] = IoArgoprojEventsV1alpha1KafkaEventSource
    globals()['IoArgoprojEventsV1alpha1MQTTEventSource'] = IoArgoprojEventsV1alpha1MQTTEventSource
    globals()['IoArgoprojEventsV1alpha1NATSEventsSource'] = IoArgoprojEventsV1alpha1NATSEventsSource
    globals()['IoArgoprojEventsV1alpha1NSQEventSource'] = IoArgoprojEventsV1alpha1NSQEventSource
    globals()['IoArgoprojEventsV1alpha1PubSubEventSource'] = IoArgoprojEventsV1alpha1PubSubEventSource
    globals()['IoArgoprojEventsV1alpha1PulsarEventSource'] = IoArgoprojEventsV1alpha1PulsarEventSource
    globals()['IoArgoprojEventsV1alpha1RedisEventSource'] = IoArgoprojEventsV1alpha1RedisEventSource
    globals()['IoArgoprojEventsV1alpha1ResourceEventSource'] = IoArgoprojEventsV1alpha1ResourceEventSource
    globals()['IoArgoprojEventsV1alpha1S3Artifact'] = IoArgoprojEventsV1alpha1S3Artifact
    globals()['IoArgoprojEventsV1alpha1SNSEventSource'] = IoArgoprojEventsV1alpha1SNSEventSource
    globals()['IoArgoprojEventsV1alpha1SQSEventSource'] = IoArgoprojEventsV1alpha1SQSEventSource
    globals()['IoArgoprojEventsV1alpha1Service'] = IoArgoprojEventsV1alpha1Service
    globals()['IoArgoprojEventsV1alpha1SlackEventSource'] = IoArgoprojEventsV1alpha1SlackEventSource
    globals()['IoArgoprojEventsV1alpha1StorageGridEventSource'] = IoArgoprojEventsV1alpha1StorageGridEventSource
    globals()['IoArgoprojEventsV1alpha1StripeEventSource'] = IoArgoprojEventsV1alpha1StripeEventSource
    globals()['IoArgoprojEventsV1alpha1Template'] = IoArgoprojEventsV1alpha1Template
    globals()['IoArgoprojEventsV1alpha1WebhookContext'] = IoArgoprojEventsV1alpha1WebhookContext


class IoArgoprojEventsV1alpha1EventSourceSpec(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'amqp': ({str: (IoArgoprojEventsV1alpha1AMQPEventSource,)},),  # noqa: E501
            'azure_events_hub': ({str: (IoArgoprojEventsV1alpha1AzureEventsHubEventSource,)},),  # noqa: E501
            'bitbucketserver': ({str: (IoArgoprojEventsV1alpha1BitbucketServerEventSource,)},),  # noqa: E501
            'calendar': ({str: (IoArgoprojEventsV1alpha1CalendarEventSource,)},),  # noqa: E501
            'emitter': ({str: (IoArgoprojEventsV1alpha1EmitterEventSource,)},),  # noqa: E501
            'event_bus_name': (str,),  # noqa: E501
            'file': ({str: (IoArgoprojEventsV1alpha1FileEventSource,)},),  # noqa: E501
            'generic': ({str: (IoArgoprojEventsV1alpha1GenericEventSource,)},),  # noqa: E501
            'github': ({str: (IoArgoprojEventsV1alpha1GithubEventSource,)},),  # noqa: E501
            'gitlab': ({str: (IoArgoprojEventsV1alpha1GitlabEventSource,)},),  # noqa: E501
            'hdfs': ({str: (IoArgoprojEventsV1alpha1HDFSEventSource,)},),  # noqa: E501
            'kafka': ({str: (IoArgoprojEventsV1alpha1KafkaEventSource,)},),  # noqa: E501
            'minio': ({str: (IoArgoprojEventsV1alpha1S3Artifact,)},),  # noqa: E501
            'mqtt': ({str: (IoArgoprojEventsV1alpha1MQTTEventSource,)},),  # noqa: E501
            'nats': ({str: (IoArgoprojEventsV1alpha1NATSEventsSource,)},),  # noqa: E501
            'nsq': ({str: (IoArgoprojEventsV1alpha1NSQEventSource,)},),  # noqa: E501
            'pub_sub': ({str: (IoArgoprojEventsV1alpha1PubSubEventSource,)},),  # noqa: E501
            'pulsar': ({str: (IoArgoprojEventsV1alpha1PulsarEventSource,)},),  # noqa: E501
            'redis': ({str: (IoArgoprojEventsV1alpha1RedisEventSource,)},),  # noqa: E501
            'replicas': (int,),  # noqa: E501
            'resource': ({str: (IoArgoprojEventsV1alpha1ResourceEventSource,)},),  # noqa: E501
            'service': (IoArgoprojEventsV1alpha1Service,),  # noqa: E501
            'slack': ({str: (IoArgoprojEventsV1alpha1SlackEventSource,)},),  # noqa: E501
            'sns': ({str: (IoArgoprojEventsV1alpha1SNSEventSource,)},),  # noqa: E501
            'sqs': ({str: (IoArgoprojEventsV1alpha1SQSEventSource,)},),  # noqa: E501
            'storage_grid': ({str: (IoArgoprojEventsV1alpha1StorageGridEventSource,)},),  # noqa: E501
            'stripe': ({str: (IoArgoprojEventsV1alpha1StripeEventSource,)},),  # noqa: E501
            'template': (IoArgoprojEventsV1alpha1Template,),  # noqa: E501
            'webhook': ({str: (IoArgoprojEventsV1alpha1WebhookContext,)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'amqp': 'amqp',  # noqa: E501
        'azure_events_hub': 'azureEventsHub',  # noqa: E501
        'bitbucketserver': 'bitbucketserver',  # noqa: E501
        'calendar': 'calendar',  # noqa: E501
        'emitter': 'emitter',  # noqa: E501
        'event_bus_name': 'eventBusName',  # noqa: E501
        'file': 'file',  # noqa: E501
        'generic': 'generic',  # noqa: E501
        'github': 'github',  # noqa: E501
        'gitlab': 'gitlab',  # noqa: E501
        'hdfs': 'hdfs',  # noqa: E501
        'kafka': 'kafka',  # noqa: E501
        'minio': 'minio',  # noqa: E501
        'mqtt': 'mqtt',  # noqa: E501
        'nats': 'nats',  # noqa: E501
        'nsq': 'nsq',  # noqa: E501
        'pub_sub': 'pubSub',  # noqa: E501
        'pulsar': 'pulsar',  # noqa: E501
        'redis': 'redis',  # noqa: E501
        'replicas': 'replicas',  # noqa: E501
        'resource': 'resource',  # noqa: E501
        'service': 'service',  # noqa: E501
        'slack': 'slack',  # noqa: E501
        'sns': 'sns',  # noqa: E501
        'sqs': 'sqs',  # noqa: E501
        'storage_grid': 'storageGrid',  # noqa: E501
        'stripe': 'stripe',  # noqa: E501
        'template': 'template',  # noqa: E501
        'webhook': 'webhook',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """IoArgoprojEventsV1alpha1EventSourceSpec - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            amqp ({str: (IoArgoprojEventsV1alpha1AMQPEventSource,)}): [optional]  # noqa: E501
            azure_events_hub ({str: (IoArgoprojEventsV1alpha1AzureEventsHubEventSource,)}): [optional]  # noqa: E501
            bitbucketserver ({str: (IoArgoprojEventsV1alpha1BitbucketServerEventSource,)}): [optional]  # noqa: E501
            calendar ({str: (IoArgoprojEventsV1alpha1CalendarEventSource,)}): [optional]  # noqa: E501
            emitter ({str: (IoArgoprojEventsV1alpha1EmitterEventSource,)}): [optional]  # noqa: E501
            event_bus_name (str): [optional]  # noqa: E501
            file ({str: (IoArgoprojEventsV1alpha1FileEventSource,)}): [optional]  # noqa: E501
            generic ({str: (IoArgoprojEventsV1alpha1GenericEventSource,)}): [optional]  # noqa: E501
            github ({str: (IoArgoprojEventsV1alpha1GithubEventSource,)}): [optional]  # noqa: E501
            gitlab ({str: (IoArgoprojEventsV1alpha1GitlabEventSource,)}): [optional]  # noqa: E501
            hdfs ({str: (IoArgoprojEventsV1alpha1HDFSEventSource,)}): [optional]  # noqa: E501
            kafka ({str: (IoArgoprojEventsV1alpha1KafkaEventSource,)}): [optional]  # noqa: E501
            minio ({str: (IoArgoprojEventsV1alpha1S3Artifact,)}): [optional]  # noqa: E501
            mqtt ({str: (IoArgoprojEventsV1alpha1MQTTEventSource,)}): [optional]  # noqa: E501
            nats ({str: (IoArgoprojEventsV1alpha1NATSEventsSource,)}): [optional]  # noqa: E501
            nsq ({str: (IoArgoprojEventsV1alpha1NSQEventSource,)}): [optional]  # noqa: E501
            pub_sub ({str: (IoArgoprojEventsV1alpha1PubSubEventSource,)}): [optional]  # noqa: E501
            pulsar ({str: (IoArgoprojEventsV1alpha1PulsarEventSource,)}): [optional]  # noqa: E501
            redis ({str: (IoArgoprojEventsV1alpha1RedisEventSource,)}): [optional]  # noqa: E501
            replicas (int): [optional]  # noqa: E501
            resource ({str: (IoArgoprojEventsV1alpha1ResourceEventSource,)}): [optional]  # noqa: E501
            service (IoArgoprojEventsV1alpha1Service): [optional]  # noqa: E501
            slack ({str: (IoArgoprojEventsV1alpha1SlackEventSource,)}): [optional]  # noqa: E501
            sns ({str: (IoArgoprojEventsV1alpha1SNSEventSource,)}): [optional]  # noqa: E501
            sqs ({str: (IoArgoprojEventsV1alpha1SQSEventSource,)}): [optional]  # noqa: E501
            storage_grid ({str: (IoArgoprojEventsV1alpha1StorageGridEventSource,)}): [optional]  # noqa: E501
            stripe ({str: (IoArgoprojEventsV1alpha1StripeEventSource,)}): [optional]  # noqa: E501
            template (IoArgoprojEventsV1alpha1Template): [optional]  # noqa: E501
            webhook ({str: (IoArgoprojEventsV1alpha1WebhookContext,)}): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """IoArgoprojEventsV1alpha1EventSourceSpec - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            amqp ({str: (IoArgoprojEventsV1alpha1AMQPEventSource,)}): [optional]  # noqa: E501
            azure_events_hub ({str: (IoArgoprojEventsV1alpha1AzureEventsHubEventSource,)}): [optional]  # noqa: E501
            bitbucketserver ({str: (IoArgoprojEventsV1alpha1BitbucketServerEventSource,)}): [optional]  # noqa: E501
            calendar ({str: (IoArgoprojEventsV1alpha1CalendarEventSource,)}): [optional]  # noqa: E501
            emitter ({str: (IoArgoprojEventsV1alpha1EmitterEventSource,)}): [optional]  # noqa: E501
            event_bus_name (str): [optional]  # noqa: E501
            file ({str: (IoArgoprojEventsV1alpha1FileEventSource,)}): [optional]  # noqa: E501
            generic ({str: (IoArgoprojEventsV1alpha1GenericEventSource,)}): [optional]  # noqa: E501
            github ({str: (IoArgoprojEventsV1alpha1GithubEventSource,)}): [optional]  # noqa: E501
            gitlab ({str: (IoArgoprojEventsV1alpha1GitlabEventSource,)}): [optional]  # noqa: E501
            hdfs ({str: (IoArgoprojEventsV1alpha1HDFSEventSource,)}): [optional]  # noqa: E501
            kafka ({str: (IoArgoprojEventsV1alpha1KafkaEventSource,)}): [optional]  # noqa: E501
            minio ({str: (IoArgoprojEventsV1alpha1S3Artifact,)}): [optional]  # noqa: E501
            mqtt ({str: (IoArgoprojEventsV1alpha1MQTTEventSource,)}): [optional]  # noqa: E501
            nats ({str: (IoArgoprojEventsV1alpha1NATSEventsSource,)}): [optional]  # noqa: E501
            nsq ({str: (IoArgoprojEventsV1alpha1NSQEventSource,)}): [optional]  # noqa: E501
            pub_sub ({str: (IoArgoprojEventsV1alpha1PubSubEventSource,)}): [optional]  # noqa: E501
            pulsar ({str: (IoArgoprojEventsV1alpha1PulsarEventSource,)}): [optional]  # noqa: E501
            redis ({str: (IoArgoprojEventsV1alpha1RedisEventSource,)}): [optional]  # noqa: E501
            replicas (int): [optional]  # noqa: E501
            resource ({str: (IoArgoprojEventsV1alpha1ResourceEventSource,)}): [optional]  # noqa: E501
            service (IoArgoprojEventsV1alpha1Service): [optional]  # noqa: E501
            slack ({str: (IoArgoprojEventsV1alpha1SlackEventSource,)}): [optional]  # noqa: E501
            sns ({str: (IoArgoprojEventsV1alpha1SNSEventSource,)}): [optional]  # noqa: E501
            sqs ({str: (IoArgoprojEventsV1alpha1SQSEventSource,)}): [optional]  # noqa: E501
            storage_grid ({str: (IoArgoprojEventsV1alpha1StorageGridEventSource,)}): [optional]  # noqa: E501
            stripe ({str: (IoArgoprojEventsV1alpha1StripeEventSource,)}): [optional]  # noqa: E501
            template (IoArgoprojEventsV1alpha1Template): [optional]  # noqa: E501
            webhook ({str: (IoArgoprojEventsV1alpha1WebhookContext,)}): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
