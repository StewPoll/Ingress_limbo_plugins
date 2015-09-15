# Ingress Limbo Plugins
This repository is a set of plugins for the slack chat bot, Limbo.
https://github.com/llimllib/limbo

## Installation
* Download the relevant files you wish to use
* Place them within limbo/plugins/
* Restart Limbo
Some plugins will require downloading images from the assets folder, and uploading as custom emoji.

## Plugins
More to come!

### Level
Allows users to calculate AP and Badge requirement for the specified level.
Usage:
    !level <number>
Result:
    Requirements for level <number>:
    AP Requirements: <value>
    Badge Requirements (if relevant)

Required:
The following images from assets should be uploaded as the relevant emojis
* badge_bronze
* badge_silver
* badge_gold
* badge_platinum
* badge_black

### Checkpoint
Gives the end of the current Cycle, and the next checkpoint.
Usage:
    !cycle
    OR
    !checkpoint
Result:
    Next CP#15 in: 4:22, at: 04:00 
    Cycle ends in 4 days 8 hours 22 mins at 2015-09-20 08:00

## Contribution
Make a pull request!
Fork away!

