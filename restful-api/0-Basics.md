# Basics of HTTP/HTTPS

## definition

H > Hyper
T > Text
T > Transfer
P > Protocol
S > Secure

## 1-difference

HTTPS is a secure version of HTTP that allows each step on a web page to be verified,
so HTTPS is more secure than HTTP.

<img src ="https://www.cloudflare.com/img/learning/security/glossary/what-is-ssl/http-vs-https.svg">

## 2-A depiction or outline HTTP

HTTP is a protocol for retrieving resources such as HTML documents.
It is the basis for all data exchange on the Web.
It is a client-server protocol, which means that requests are initiated by the recipient
(usually a web browser).
A complete document is constructed from various sub-documents that are retrieved,
for example text, layout descriptions, images, videos, scripts and much more.

<img src ="https://developer.mozilla.org/fr/docs/Web/HTTP/Overview/fetching_a_page.png">


## 3-Lists of common HTTP methods and status codes

HTTP request methods

These are the nine HTTP methods typically associated with RESTful web development and the Hypertext Transfer Protocol and most commonly used by RESTful API designers:

### ***GET.***

The purpose of the GET method is to simply retrieve data from the server. The GET method is used to request any of the following resources:

. A webpage or HTML file.
. An image or video.
. A JSON document.
. A CSS file or JavaScript file.
. An XML file.

### ***PUT.***

The HTTP PUT method is used to completely replace a resource identified with a given URL.

The HTTP PUT request method includes two rules:

A PUT operation always includes a payload that describes a completely new resource definition to be saved by the server.
The PUT operation uses the exact URL of the target resource.
If a resource exists at the URL provided by a PUT operation, the resource’s representation is completely replaced. If a resource does not exist at that URL, a new resource is created.

The payload of a PUT operation can be anything that the server understands, although JSON and XML are the most common data exchange formats for RESTful webservices and microservices.

### ***POST.***

The POST HTTP request method sends data to the server for processing.

The data sent to the server is typically in the following form:

. Input fields from online forms.
. XML or JSON data.
. Text data from query parameters.

### ***DELETE.***

The HTTP DELETE method is self-explanatory. After execution, the resource a DELETE operation points to is removed from the server.
PATCH.
HEAD.
OPTIONS.
TRACE.
CONNECT.
