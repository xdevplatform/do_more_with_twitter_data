
Working with the API within a Python program is straightforward both for
Premium and Enterprise clients.

We’ll assume that credentials are in the default location,
``~/.twitter_keys.yaml``.

.. code:: ipython3

    from searchtweets import ResultStream, gen_rule_payload, load_credentials

Enterprise setup
----------------

.. code:: ipython3

    enterprise_search_args = load_credentials("~/.twitter_keys.yaml",
                                              yaml_key="search_tweets_enterprise",
                                              env_overwrite=False)

Premium Setup
-------------

.. code:: ipython3

    premium_search_args = load_credentials("~/.twitter_keys.yaml",
                                           yaml_key="search_tweets_premium_30day",
                                           env_overwrite=False)

There is a function that formats search API rules into valid json
queries called ``gen_rule_payload``. It has sensible defaults, such as
pulling more Tweets per call than the default 100 (but note that a
sandbox environment can only have a max of 100 here, so if you get
errors, please check this) not including dates, and defaulting to hourly
counts when using the counts api. Discussing the finer points of
generating search rules is out of scope for these examples; I encourage
you to see the docs to learn the nuances within, but for now let’s see
what a rule looks like.

.. code:: ipython3

    rule = gen_rule_payload("beyonce", results_per_call=100) # testing with a sandbox account
    print(rule)


.. parsed-literal::

    {"query":"beyonce","maxResults":100}


This rule will match tweets that have the text ``beyonce`` in them.

From this point, there are two ways to interact with the API. There is a
quick method to collect smaller amounts of Tweets to memory that
requires less thought and knowledge, and interaction with the
``ResultStream`` object which will be introduced later.

Fast Way
--------

We’ll use the ``search_args`` variable to power the configuration point
for the API. The object also takes a valid PowerTrack rule and has
options to cutoff search when hitting limits on both number of Tweets
and API calls.

We’ll be using the ``collect_results`` function, which has three
parameters.

-  rule: a valid PowerTrack rule, referenced earlier
-  max_results: as the API handles pagination, it will stop collecting
   when we get to this number
-  result_stream_args: configuration args that we’ve already specified.

For the remaining examples, please change the args to either premium or
enterprise depending on your usage.

Let’s see how it goes:
