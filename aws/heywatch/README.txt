aws.heywatch Package Readme
=========================

Overview
--------

Hey!Watch is an online video encoding service.

This package allows to upload a video to Hey!Watch, let them encode the video,
then retrieve and store the encoded file.

First implementation has been done for the "WaveBack" project.
http://waveback.net

It provides several components:

- a heywatch library to use heywatch
- a zope interface exposing heywatch features
- a global utility to access heywatch
- an adapter on video files to provide heywatch features
- a content provider to display the upload and conversion status
- an upload content provider to send directly to heywatch without storing the
  original video.

Uploading is done asynchronously with zc.async

To use this component, you must configure your Heywatch user:pass in the
~/.heywatch file.

Heywatch library
----------------

>>> from aws.heywatch.heywatch import HeyWatchService

We can get the account info:

>>> heywatch = HeyWatchService()
>>> heywatch.account # doctest: +ELLIPSIS
<Element account at ...>
>>> heywatch.account.user.firstname.tag
'firstname'
>>> type(heywatch.account.user.firstname)
<type 'lxml.objectify.StringElement'>



HeyWatch interface
------------------

The HeyWatch interface exposes the available features added to a video file:

>>> from aws.heywatch.interfaces import IHeyWatch
>>> IHeyWatch
<InterfaceClass aws.heywatch.interfaces.IHeyWatch>




