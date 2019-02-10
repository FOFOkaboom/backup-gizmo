# backup-gizmo
Backup and deploy gizmo

## Why I want this Gizmo
During my pentesting activities I find myself performing many tasks over and over again when deploying a new VM. 
I also find myself searching for notes, scripts and HOWTO's on multiple systems way too often. 
This backup Gizmo is going to centralize my scripts and knowledge repo's in an automated manner. 

## Pre-req
Define basic linux/windows system

## Research topic:
* rsync vs sftp
* Multi OS zip/crypt client (7zip?)

## Conditions
* Must be python
* Must have centralized managemend
* Keys must be stored centralized
* Authentication and authorization unique per system
* Access logging
* Action notifycation
* Archived files must be compressed 
* Archived (encrypted) files must be decryptable/decompressable on any OS. 

## Functions
* [F01] Setup unattended SFTP server 
* [F02] Setup unattended SFTP Client
* [F03] Setup unattended SSH Client
* [F04] Sync with DropBox pull
* [F05] Sync with DropBox push
* [F06] Sync with SFTP pull 
* [F07] Sync with SFTP push 
* [F08] Sync with (rsync via SSH) pull 
* [F09] Sync with (rsync via SSH) push 
* [F10] Encrypt files while performing push
* [F11] Decrypt files while performing pull
* [F12] Email notification
* [F13] Push new encryption keys to clients
* [F14] Configure Basic system (linux)
* [F15] Configure Basic system (Windows)
* [F16] Share files publicly via github

## Roadmap
TBD
