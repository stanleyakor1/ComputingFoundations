from cache import *
from sys import *

option = int(argv[1])

if option == 1:
	# One level cache
    cache = OneLevel_Cache(int(argv[2]))

    with open(argv[3],'r') as file:
        for line in file:
            for word in line.split():
                try:
                    cache.search(word)
                except:
                    print('Some issues encountered')
    hit_ratio=cache.hit_ratio()
    hit,mis=cache.Info()
    print()
    print(f'One level cache with {argv[2]} entries was created')
    print()
    print(f'The number of cache references: {hit+mis}')
    print(f'The number of One level cache hits: {hit}')
    print('The One level cache hit ratio',' '*23,':',hit_ratio)
    print('-'*75)

elif option == 2:
	# Two level Cache
    cache = TwoLevel_Cache(int(argv[2]),int(argv[3]))

    with open(argv[4],'r') as file:
        for line in file:
            for word in line.split():
               try:
                   cache.search(word)
               except:
                   print('Some issues encountered')
                    
    hr1=cache.cache1_hitratio()
    hr2=cache.cache2_hitratio()
    hr=cache.global_hitratio()
    c1_hit,c1_miss,c2_hit,c2_miss=cache.Info()
    print()
    print(f'First level cache with {argv[2]} entries was created')
    print(f'Second level cache with {argv[3]} entries was created')
    print()

    print(f'The number of global references: {c1_hit+c1_miss}')
    print(f'The number of global cache hits: {c1_hit+c2_hit}')
    print('global hit ratio',' '*23,':', hr)
    print()

    print(f'The number of 1st-level references:  {c1_miss+c1_hit}')
    print(f'The number of 1st-level cache hit:  {c1_hit}')
    print('The 1st-level cache hit ratio',' '*9,':',hr1)
    print()

    print(f'The number of 2nd-level references:  {c1_miss}')
    print(f'The number of 2nd-level cache hit: {c2_hit}')
    print('The 2nd-level cache hit ratio',' '*9,':', hr2)
    print('-'*75)
else:
    print('You have entered an invalid option')
