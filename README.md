![Supported Python versions](https://img.shields.io/badge/python-3.6+-blue.svg) [![Documentation Status](https://readthedocs.org/projects/msldap/badge/?version=latest)](https://msldap.readthedocs.io/en/latest/?badge=latest) [![Twitter](https://img.shields.io/twitter/follow/skelsec?label=skelsec&style=social)](https://twitter.com/intent/follow?screen_name=skelsec)

## :triangular_flag_on_post: Sponsors

If you like this project, consider purchasing licenses of [OctoPwn](https://octopwn.com/), our full pentesting suite that runs in your browser!  
For notifications on new builds/releases and other info, hop on to our [Discord](https://discord.gg/PM8utcNxMS)


# adiskreader-secretsdump
Extract registry and NTDS secrets from local or remote disk images

## :triangular_flag_on_post: Runs in the browser

This project, alongside with many other pentester tools runs in the browser with the power of OctoPwn!  
Check out the community version at [OctoPwn - Live](https://live.octopwn.com/)


# Install
`git clone` then `pip install .`

# Usage
First you MUST manually install `adiskreader` project from [here](https://github.com/skelsec/adiskreader) as it is not yet packaged on pip.  
after install you'll get `adiskreacer-secretsdump`. Just use `adiskreacer-secretsdump <url>` 

## Commands
The command line argument of this tool has the same format as the adiskreader-console.  
Examples:

### Parsing a VHDX file over SMB
`adiskreader-secretsdump smb+ntlm-password://TEST\victim@10.10.10.2/sharename/foldername/disk.vhdx`  

### Parsing a VHD file over SSH
`adiskreader-secretsdump ssh+password+vhd://test:test@10.10.10.3/mnt/hgfs/vhdxtest/17763.737.amd64fre.rs5_release_svc_refresh.190906-2324_server_serverdatacentereval_en-us_1.vhd`  