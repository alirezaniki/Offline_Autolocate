# Offline_Autolocate
Offline_Autolocate is a bash script to run an autolocation process on a Mseed data or SDS archive using seiscomp3

Use ./Playback -h to see help message

Usage Example:

Database="mysql://sysop:sysop@localhost/seiscomp3"

./Playback -f PrepairedData.mseed -d $Database -n IR

./Playback -a ./Archive/ -t '2019-03-13 08:51:00~2019-03-13 09:00:00' -n IRIS -d $Database

Requirements
------------

Seiscomp3

TIPS
----

Please complete the main headers (network, station, channel) in the input mseed file before proceeding.
