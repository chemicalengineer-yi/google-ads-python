# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v2.proto.services import reach_plan_service_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2


class ReachPlanServiceStub(object):
  """Proto file describing the reach plan service.

  Reach Plan Service gives users information about audience size that can
  be reached through advertisement on YouTube. In particular,
  GenerateReachForecast provides estimated number of people of specified
  demographics that can be reached by an ad in a given market by a campaign of
  certain duration with a defined budget.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListPlannableLocations = channel.unary_unary(
        '/google.ads.googleads.v2.services.ReachPlanService/ListPlannableLocations',
        request_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.ListPlannableLocationsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.ListPlannableLocationsResponse.FromString,
        )
    self.ListPlannableProducts = channel.unary_unary(
        '/google.ads.googleads.v2.services.ReachPlanService/ListPlannableProducts',
        request_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.ListPlannableProductsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.ListPlannableProductsResponse.FromString,
        )
    self.GenerateProductMixIdeas = channel.unary_unary(
        '/google.ads.googleads.v2.services.ReachPlanService/GenerateProductMixIdeas',
        request_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.GenerateProductMixIdeasRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.GenerateProductMixIdeasResponse.FromString,
        )
    self.GenerateReachForecast = channel.unary_unary(
        '/google.ads.googleads.v2.services.ReachPlanService/GenerateReachForecast',
        request_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.GenerateReachForecastRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.GenerateReachForecastResponse.FromString,
        )


class ReachPlanServiceServicer(object):
  """Proto file describing the reach plan service.

  Reach Plan Service gives users information about audience size that can
  be reached through advertisement on YouTube. In particular,
  GenerateReachForecast provides estimated number of people of specified
  demographics that can be reached by an ad in a given market by a campaign of
  certain duration with a defined budget.
  """

  def ListPlannableLocations(self, request, context):
    """Returns the list of plannable locations (for example, countries & DMAs).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPlannableProducts(self, request, context):
    """Returns the list of per-location plannable YouTube ad formats with allowed
    targeting.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenerateProductMixIdeas(self, request, context):
    """Generates a product mix ideas given a set of preferences. This method
    helps the advertiser to obtain a good mix of ad formats and budget
    allocations based on its preferences.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenerateReachForecast(self, request, context):
    """Generates a reach forecast for a given targeting / product mix.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ReachPlanServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListPlannableLocations': grpc.unary_unary_rpc_method_handler(
          servicer.ListPlannableLocations,
          request_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.ListPlannableLocationsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.ListPlannableLocationsResponse.SerializeToString,
      ),
      'ListPlannableProducts': grpc.unary_unary_rpc_method_handler(
          servicer.ListPlannableProducts,
          request_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.ListPlannableProductsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.ListPlannableProductsResponse.SerializeToString,
      ),
      'GenerateProductMixIdeas': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateProductMixIdeas,
          request_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.GenerateProductMixIdeasRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.GenerateProductMixIdeasResponse.SerializeToString,
      ),
      'GenerateReachForecast': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateReachForecast,
          request_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.GenerateReachForecastRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_reach__plan__service__pb2.GenerateReachForecastResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v2.services.ReachPlanService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
