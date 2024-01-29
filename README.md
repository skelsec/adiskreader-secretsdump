# adiskreader-secretsdump
Extract registry and NTDS secrets from local or remote disk images

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