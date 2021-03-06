"""
Variables related to data or storage
"""
# Blob Storage credentials
STORAGE_ACCOUNT = 'kehuanamlstorage'
STORAGE_KEY = 'F2C0yr/S5/rLWw3Yut/1Y1SXKSlBhDpHMeFz+uzUuWfBlqLJG2BJk8/09tQfhr3uzfRtFW7jCPb0j0+m21QYJw=='
CONTAINER = 'document-collection-analysis'

# The AMLWorkbench folder used to save intermediate files in a run
OUTPUT_PATH = 'outputs'

# The dataset file name
DATASET_FILE = 'CongressionalDataAll_Jun_2017.tsv'
# DATASET_FILE = 'small_data.tsv'

# The black list of words to ignore
BLACK_LIST_FILE = 'black_list.txt'

# The non-content bearing function words
FUNCTION_WORDS_FILE = 'function_words.txt'


"""
Variables related to intermediate files
"""
# The file name used to save the cleaned and sentenced text data
CLEANED_DATA_FILE_NAME = 'CongressionalDocsCleaned.tsv'
# CLEANED_DATA_FILE_NAME = 'CongressionalDocsCleaned_Small.tsv'

# The learned phrases file
# The file name will be renamed in the format of <file_name>_phrase_<MAX_NUM_PHRASE>.txt
LEARNED_PHRASES_FILE = 'CongressionalDocsLearnedPhrases.txt'
# LEARNED_PHRASES_FILE = 'CongressionalDocsLearnedPhrases_Small.txt'

# The text data with phrase rewrites
# The file name will be renamed in the format of <file_name>_phrase_<MAX_NUM_PHRASE>.txt
PHRASE_TEXT_FILE = 'CongressionalDocsPhraseTextData.txt'
# PHRASE_TEXT_FILE = 'CongressionalDocsPhraseTextData_Small.txt'

# The model vocabulary and surface form mapping file
# The file name will be renamed in the format of <file_name>_phrase_<MAX_NUM_PHRASE>.txt
SURFACE_MAPPING_FILE = 'Vocab2SurfaceFormMapping.tsv'
# SURFACE_MAPPING_FILE = 'Vocab2SurfaceFormMapping_Small.tsv'

# The reconstituted text file name
# The file name will be renamed in the format of <file_name>_phrase_<MAX_NUM_PHRASE>.txt
RECONSTITUTED_TEXT_FILE = 'CongressionalDocsProcessed.tsv'
# RECONSTITUTED_TEXT_FILE = 'CongressionalDocsProcessed_Small.tsv'



"""
Variables related to run configuration
"""
# Maximum number of phrases to learn
MAX_NUM_PHRASE = 25000
# MAX_NUM_PHRASE = 2000       # for small dataset

# Maximum number of phrases to learn per iteration
MAX_PHRASE_PER_ITER = 500

# Maximum number of words allowed in the learned phrases
MAX_PHRASE_LENGTH = 7

# Minimum number of times a phrase must occur in the data to
# be considered during the phrase learning process
MIN_INSTANCE_COUNT = 5


"""
Variables related to train the LDA topic model
"""
# Minimum word count in the corpus
MIN_WORD_COUNT = 5

# Minimum count of documents that contain a specific word
MIN_DOC_COUNT = 2

# The maximum document frequency that contain a specific word
MAX_DOC_FREQ = 0.25

# The number of topics need to train
NUM_TOPICS = 20
# NUM_TOPICS = 20       # for small dataset

# The number of iterations during training the LDA model
NUM_ITERATIONS = 2000

# Number of passes through the entire corpus
NUM_PASSES = 10
# NUM_PASSES = 5       # for small dataset

# Number of documents to load into memory at a time and process E step of EM
CHUNK_SIZE = 1000

# The random number during training the LDA model
RANDOM_STATE = 1

# The file name of LDA model file
# This file name will be automatically renamed in the format of:
# <file_name>_<MAX_NUM_PHRASE>_<NUM_TOPICS>_<NUM_ITERATIONS>_<NUM_PASSES>_<CHUNK_SIZE>.pickle
LDA_FILE = "CongressionalDocsLDA.pickle"

# The transformed document topic probability matrix file
# This file name will be automatically renamed in the format of:
# <file_name>_<MAX_NUM_PHRASE>_<NUM_TOPICS>_<NUM_ITERATIONS>_<NUM_PASSES>_<CHUNK_SIZE>.npy
DOC_TOPIC_PROB_FILE = "CongressionalDocTopicProbs.npy"


