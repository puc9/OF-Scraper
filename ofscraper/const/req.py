CONNECT_TIMEOUT = 100
POOL_CONNECT_TIMEOUT = 100
MAX_CONNECTIONS = 100
API_MAX_CONNECTION = 100
CHUNK_READ_TIMEOUT = 100
TOTAL_TIMEOUT = None
DISCORD_TOTAL_TIMEOUT = 20
CDM_TEST_TIMEOUT = 30
CDM_TIMEOUT = 40
KEEP_ALIVE = 20
KEEP_ALIVE_EXP = 10
PROXY = None
PROXY_MOUNTS = None
PROXY_AUTH = None
maxChunkSize = 1024 * 1024 * 10
maxChunkSizeB = 1024 * 1024
CHUNK_ITER = 10

REQ_SEMAPHORE_MULTI = 5
API_REQ_SEM_MAX = 12
SCRAPE_PAID_SEMS = 10
SUBSCRIPTION_SEMS = 5
API_REQ_CHECK_MAX = 12
LIKE_MAX_SEMS = 12
MAX_SEMS_BATCH_DOWNLOAD = 12
MAX_SEMS_SINGLE_THREAD_DOWNLOAD = 50
MPD_MAX_SEMS = 4
SESSION_MANAGER_SYNC_SEM_DEFAULT = 3
SESSION_MANAGER_SEM_DEFAULT = 10

OF_MIN_WAIT_SESSION_DEFAULT = 4
OF_MAX_WAIT_SESSION_DEFAULT = 12
OF_MIN_WAIT_EXPONENTIAL_SESSION_DEFAULT = 8
OF_MAX_WAIT_EXPONENTIAL_SESSION_DEFAULT = 128
OF_NUM_RETRIES_SESSION_DEFAULT = 10


OF_MIN_WAIT_API = 10
OF_MAX_WAIT_API = 20
OF_AUTH_MIN_WAIT = 3
OF_AUTH_MAX_WAIT = 10
GIT_MIN_WAIT = 1
GIT_MAX_WAIT = 5
DISCORD_MIN_WAIT = 1
DISCORD_MAX_WAIT = 5
CDM_MIN_WAIT = 1
CDM_MAX_WAIT = 5

DOWNLOAD_FILE_NUM_TRIES = 3
DOWNLOAD_FILE_NUM_TRIES_CHECK = 1
DOWNLOAD_NUM_TRIES = 5
DOWNLOAD_RETRIES_NUM_TRIES = 1
API_NUM_TRIES = 10
API_LIKE_NUM_TRIES = 5
AUTH_NUM_TRIES = 3
GIT_NUM_TRIES = 3
CDM_NUM_TRIES = 5
CDM_TEST_NUM_TRIES = 2
DISCORD_NUM_TRIES = 3
MPD_NUM_TRIES = 5
API_INDVIDIUAL_NUM_TRIES = 3
API_PAID_NUM_TRIES = 8
API_CHECK_NUM_TRIES = 10


MAX_THREAD_WORKERS = 20
API_MAX_AREAS = 2
API_TIMEOUT_PER_TASK = 500
API_REQUEST_THREADONLY = ["Windows", "Linux", "Darwin"]

# page must be 50 post, and 50 is a reasonable size for max number of pages
REASONABLE_MAX_PAGE = 50
MIN_PAGE_POST_COUNT = 50
# messages
REASONABLE_MAX_PAGE_MESSAGES = 80
