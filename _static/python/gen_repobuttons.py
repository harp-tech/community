# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:47:25 2022

@author: Alex
"""

 devicePage.replace('GITHUBLINK', devicedata[count].get("github"))
 devicePage.replace('GITHUBLINK', devicedata[count].get("bitbucket"))

bitbucketlink = devicedata[count].get("bitbucket")

if bitbucketlink == '':
    repoButtonBB = bitbucketlink
else:
    repoButtonBB = repoButton.replace('REPOLINK', bitbucketlink)
    repoButtonBB = repoButton.replace('WHICHREPO', "bitbucket")

githublink = devicedata[count].get("github")

if githublink == '':
    repoButtonGH = githublink
else:
    repoButtonGH = repoButton.replace('REPOLINK', githublink)
    repoButtonGH = repoButton.replace('WHICHREPO', "github")


REPOBUTTONS