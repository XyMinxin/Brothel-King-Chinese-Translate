#### BUILD DISTRIBUTION ####

## The purpose of this file is to track the distribution version of BK to identify when players
## have installed a patch on top of an older version (common problem).
## It is only distributed with the full version, so that it won't be overwritten by a patch.
## Test version numbers are followed by "t" to differentiate them from releases "r".

init -2 python:
    BK_DIST = "0.3t"

#### END ####
