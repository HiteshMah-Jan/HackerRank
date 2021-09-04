class NodeData:  # pylint: disable=too-few-public-methods
"""
Represents a nav_node which has a pvid (HERE spec) and all of the nav links related to
it.
TODO - convert to dataclass
"""

class NodeData:  # pylint: disable=too-few-public-methods
"""
Represents a nav_node which has a pvid (HERE spec) and all of the nav links related to
it.
TODO - convert to dataclass
"""

"""
The relation between a SearchPlace and its Phones. See `ContactInfoAttribute
<https://developer.here.com/olp/documentation/here-map-content/topics_api/com.here.schema.rib.v2.contactinfoattribute.html>`_
where the `type` is `PHONE` or `FAX` or `MOBILE_PHONE` or `TOLL_FREE`.
"""


@doc.parameter("node_label", _in="path", choices=sorted(GeometryForNode.Handled))
@doc.summary("Geometries for a node")
@doc.description(
"""Sometimes you want to put nodes on a map: like "where is the place that has this phone number?" """
"""or "show me what street segments are included in this district". This endpoint will walk the graph """
"""and create a "multi" geometry (for most things), or for nodes like District and "Subdistrict" """
"""it computes a derived (multi-) polygon."""

  
  
  * "reference" data - like categories, payment types, etc or,
* duplicated nodes - like Url, Phone number etc.

There are a number of "place" transforms - SearchPlace, VenueMaps, EV charging stations etc, and
they share some 2nd-order data like web-domains, phone numbers and opening times. Other datasets
  
  
  class ReviewRating(DuplicatedNode):
"""
The `FeedbackAttribute.Review.ReviewRating
<https://developer.here.com/olp/documentation/here-map-content/topics_api/com.here.schema.rib.v2.feedbackattribute.review.rating.html>`_.
"""

label: str = "ReviewRating"

  
  
  
  
  Code: `
refuel, rest, or take refreshments.
here:pds:navteq-lcms:400-4300-0308 - Scenic Overlook Rest Area
A rest area that provides a location along a roadway with a regionally important panorama or overlook, or
a place where a driver can stop to observe the scenery.

I prioritise them, from least important to most important as:
  
  
  
