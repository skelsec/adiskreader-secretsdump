import asyncio
import argparse
from adiskreader_secretsdump.utils import url_to_fs
from adiskreader_secretsdump.modules.registry import REGSecrets
from adiskreader_secretsdump.modules.ntds import NTDSSecrets

async def amain():
	parser = argparse.ArgumentParser(description='Secretsdump for adiskreader')
	parser.add_argument('-v', '--verbose', action='count', default=0)
	#parser.add_argument('-o', '--out-file', help='Output file path.')
	parser.add_argument('--pid', type=int, help='Partition index to use. This should not be needed in most cases.')
	parser.add_argument('--no-history', action='store_true', help='Do not parse history')
	parser.add_argument('url', help='Adiskreader connection URL')

	args = parser.parse_args()

	fs = await url_to_fs(args.url, args.pid)
	if fs is None:
		raise Exception('No suitable partition found!')
	
	rs = REGSecrets(fs)
	async for line in rs.run():
		print(line)

	ns = NTDSSecrets(fs, rs.result)
	ns.with_history = not args.no_history
	async for line in ns.run():
		print(line)
	
	



def main():
	asyncio.run(amain())

if __name__ == '__main__':
	main()