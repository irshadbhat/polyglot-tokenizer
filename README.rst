Tokenizer
=========

----

Tokenizer for Indian scripts and Roman script.

This module provides a complete tokenizer for Indian languages including Urdu, Kashmiri and Roman script.


Install
^^^^^^^

::

    - git clone https://irshadbhat@bitbucket.org/iscnlp/tokenizer.git
    - cd tokenizer
    - sudo python setup.py install

Tokenizer
^^^^^^^^^

.. code:: python

    >>> from __future__ import unicode_literals
    >>> from isc_tokenizer import Tokenizer
    >>> tk = Tokenizer(lang='eng', smt=True) #smt is a flag for social-media-text
    >>> text = "RT @BJP_RSS Crack down on Black money.India slides to 75th slot on Swiss bank money list #ModiForeignAchievements @RituRathaur https://t.c…"
    >>> tk.tokenize(text)
    ['RT', '@BJP_RSS', 'Crack', 'down', 'on', 'Black', 'money', '.', 'India', 'slides', 'to', '75th', 'slot', 'on', 'Swiss', 'bank', 'money', 'list', '#ModiForeignAchievements', '@RituRathaur', 'https://t.c…']
    >>> tk = Tokenizer(lang='hin')
    >>> tk.tokenize("22 साल के लंबे इंतजार के बाद आखिरकार हॉलीवुड स्टार लियोनार्डो डिकैप्रियो को अपनी पहली ऑस्कर ट्रॉफी"
    ...             " मिल चुकी है। उन्हें ये अवॉर्ड अपनी फिल्म ‘द रेवेनेंट’ में ह्यूज ग्लास के किरदार के लिए मिला, लेकिन उनके"
    ...             " के लिए रोल निभाना आसान नहीं था।")
    ['22', 'साल', 'के', 'लंबे', 'इंतजार', 'के', 'बाद', 'आखिरकार', 'हॉलीवुड', 'स्टार', 'लियोनार्डो', 'डिकैप्रियो', 'को', 'अपनी', 'पहली', 'ऑस्कर', 'ट्रॉफी', 'मिल', 'चुकी', 'है', '।', 'उन्हें', 'ये', 'अवॉर्ड', 'अपनी', 'फिल्म', "'", 'द', 'रेवेनेंट', "'", 'में', 'ह्यूज', 'ग्लास', 'के', 'किरदार', 'के', 'लिए', 'मिला', ',', 'लेकिन', 'उनके', 'के', 'लिए', 'रोल', 'निभाना', 'आसान', 'नहीं', 'था', '।']
    >>> tk = Tokenizer(lang='hin', split_sen=True)
    >>> tk.tokenize("22 साल के लंबे इंतजार के बाद आखिरकार हॉलीवुड स्टार लियोनार्डो डिकैप्रियो को अपनी पहली ऑस्कर ट्रॉफी"
    ...             " मिल चुकी है। उन्हें ये अवॉर्ड अपनी फिल्म ‘द रेवेनेंट’ में ह्यूज ग्लास के किरदार के लिए मिला, लेकिन उनके"
    ...             " के लिए रोल निभाना आसान नहीं था। फिल्म एक सीन के लिए लियोनार्डो को भैंस का कच्चा लीवर खाना"
    ...             " पड़ा था। जबकि असल जिंदगी में वो पूरी तरह शाकाहारी हैं। हालांकि इस सीन के लिए पहले लियोनार्डो को"
    ...             " मांस जैसे दिखने वाली चीज दी गई थी, लेकिन उन्हें लगा कि ऐसा करना गलत होगा। फिल्म के लिए इम्पोर्ट"
    ...             " की गई चीटियां...")
    [['22', 'साल', 'के', 'लंबे', 'इंतजार', 'के', 'बाद', 'आखिरकार', 'हॉलीवुड', 'स्टार', 'लियोनार्डो', 'डिकैप्रियो', 'को', 'अपनी', 'पहली', 'ऑस्कर', 'ट्रॉफी', 'मिल', 'चुकी', 'है', '।'], ['उन्हें', 'ये', 'अवॉर्ड', 'अपनी', 'फिल्म', "'", 'द', 'रेवेनेंट', "'", 'में', 'ह्यूज', 'ग्लास', 'के', 'किरदार', 'के', 'लिए', 'मिला', ',', 'लेकिन', 'उनके', 'के', 'लिए', 'रोल', 'निभाना', 'आसान', 'नहीं', 'था', '।'], ['फिल्म', 'एक', 'सीन', 'के', 'लिए', 'लियोनार्डो', 'को', 'भैंस', 'का', 'कच्चा', 'लीवर', 'खाना', 'पड़ा', 'था', '।'], ['जबकि', 'असल', 'जिंदगी', 'में', 'वो', 'पूरी', 'तरह', 'शाकाहारी', 'हैं', '।'], ['हालांकि', 'इस', 'सीन', 'के', 'लिए', 'पहले', 'लियोनार्डो', 'को', 'मांस', 'जैसे', 'दिखने', 'वाली', 'चीज', 'दी', 'गई', 'थी', ',', 'लेकिन', 'उन्हें', 'लगा', 'कि', 'ऐसा', 'करना', 'गलत', 'होगा', '।'], ['फिल्म', 'के', 'लिए', 'इम्पोर्ट', 'की', 'गई', 'चीटियां', '...']]

Tokenizer can also be called from Command Line Interface.

.. parsed-literal::

    irshad@iscnlp$ isc-tokenizer --h
    usage: Indic-Tokenizer [-h] [-v] [-i] [-s] [-o] [-l]
    
    Tokenizer for Indian Scripts
    
    optional arguments:
      -h, --help              show this help message and exit
      -v, --version           show program's version number and exit
      -i , --input            <input-file>
      -s, --split-sentences   set this flag to apply sentence segmentation
      -o , --output           <output-file>
      -t, --social-media-test set this flag if the input file contains social media text 
                              like twitter, facebook and whatsapp
      -l , --language         select language (3 letter ISO-639 code) {hin, urd,
                              ben, asm, guj, mal, pan, tel, tam, kan, ori, mar, nep,
                              bod, kok, kas, eng}
