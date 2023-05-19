# dnstwister_fuzz
exports fuzzing results from dnstwister api and checks for DNS resolution

1 - fuzzer.py extracts dnsTwister fuzzing results for a given name
2 - resolver.sh checks for DNS resolution for dnstwiser results
3 - cleanup manually rows ending in "-->\n"
4 - cleaner.py removes the original names from the resolved fuzz names
