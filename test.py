import requests
import hashlib
import os
HASH_1 = '098f6bcd4621d373cade4e832627b4f6'   # 'test' 
HASH_2 = 'db0f6f37ebeb6ea09489124345af2a45'   # 'group'
FIB_SEQ = [0,1,1,2,3,5,8,13,21,34]
HTTP_ENCODE = "Sorry%20about%20the%20alerts..."
print ("Testing API for expected results...\n")
tests = {
    '/md5/test':                    (200, HASH_1),
    '/md5/group':           (200, HASH_2),
    '/md5':                         (200, None),
    '/factorial/4':                 (200, 24),
    '/factorial/5':                 (200, 120),
    '/factorial/test':              (400, None),
    '/factorial/0':                 (200, 1),
    '/fibonacci/8':                 (200, FIB_SEQ[:7]),
    '/fibonacci/35':                (200, FIB_SEQ),
    '/fibonacci/test':              (400, None),
    '/fibonacci/1':                 (200, FIB_SEQ[:3]),
    '/is-prime/1':                  (200, False),
    '/is-prime/2':                  (200, True),
    '/is-prime/5':                  (200, True),
    '/is-prime/6':                  (200, False),
    '/is-prime/37':                 (200, True),
    '/slack-alert/test':            (200, True),
    '/slack-alert/'+HTTP_ENCODE:    (200, True),
    }
FAILED = 0
PASSED = 0
for uri, test_result in tests.items():
    print(" * ", uri, "... ", end=" ")
    #resp = requests.get('http://www.aslancole.com'+uri)
    resp = requests.get('http://localhost:5000'+uri)
    if resp.status_code == test_result[0]:
        if test_result[1] == None or resp.json()['output'] == test_result[1]:
            print("Congrats it Passed")
            PASSED += 1
        else:
            print("FAILED")
            print("          - Expected output: '%s'" % str(test_result[1]))
            print("          - Actual output:   '%s'" % str(resp.json()['output']))
            FAILED += 1
    else:
        print("FAILED")
        print("          - Expected HTTP status: %i" % test_result[0])
        print ("          - Actual HTTP status:   %i" % resp.status_code)
        FAILED += 1
rate = float(PASSED) / float(FAILED+PASSED) * 100.0
print ("\n\n Passed %i of %i tests (%i%% Success rate)" % (PASSED, FAILED+PASSED, rate))
