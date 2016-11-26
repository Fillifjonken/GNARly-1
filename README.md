# GNARly
A school project in the course Dynamic web systems. We are trying out docker and want to run each part on a separate docker container.

### TODO:
* Fix DNS container. Currently redirects *.gnarly.redid.nu to redid.nu(the global URL)
    * Seems to be an error with the BIND config, namely the master IP or similar
    * Maybe set BIND container itself to master?
