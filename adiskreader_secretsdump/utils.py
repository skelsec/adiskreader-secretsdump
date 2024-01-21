from adiskreader.datasource import DataSource
from adiskreader.disks import Disk

async def url_to_fs(url, partition_idx = None, fstype = 'NTFS'):
	ds = await DataSource.from_url(url)
	disk = await Disk.from_datasource(ds)
	partitions = await disk.list_partitions()
	
	if partition_idx is not None:
		return await partitions[partition_idx].mount()
	
	for partition in partitions:
		if partition.FileSytemType == fstype:
			try:
				fs = await partition.mount()
				rootdir = await fs.get_root()
				windir = await rootdir.get_child('Windows')
				if windir is not None:
					return fs
			except Exception as e:
				pass
	return None