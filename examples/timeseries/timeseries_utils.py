import re
import itertools as it
import numpy as np
import pandas as pd
from string import punctuation
import unicodedata

from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.tokenize import TweetTokenizer

# import tweepy
import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter


def plot_ts(series,
            ma=False,
            raw=False,
            expanding=False,
            ewma=False,
            overall=False,
            median=False,
            title=None,
            time_bin="hour",
            date_markers=None,
            y_label=None,
            custom_yaxis=None,
            custom_ax=None,
            **kwargs):
    """
    custom plotting function for our time-series dataframes. 

    Args:
        series: pd.Series or pd.Dataframe
        raw: plot the basic values in the frame
        expanding: plot an expanding mean
        ewma: plot an ewma line
        overall: plot an overall mean
        median: plot the overall median
        title: custom title to use
        time_bin: marks the y-axis correctly
        date_markers: plots a dot on the signal where a given date is noted.
        y_label: custom y-axis label
        custom_yaxis: custom axis
        custom_ax: passing a custom Axes here will assign this plot to that
                   axis


   """
    if isinstance(series, pd.DataFrame):
        series = series["count"]

    lw = 0.75
    if custom_ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
    else:
        ax = custom_ax

    if y_label is None:
        period = series.index.to_period().freqstr
        _bin = "day" if period == "D" else "hour"
        _y_label = "tweets per {}".format(_bin)
        plt.ylabel(_y_label)
    else:
        if isinstance(y_label, str):
            plt.ylabel(y_label)

    if date_markers is not None:
        def dateindex_to_str(index, include_hour=True):
            idx = 16 if include_hour else 10
            return [str(date)[0:idx].replace("T", " ")
                    for date in index.values]

        (ax.plot(date_markers, series.loc[date_markers],
                 "o", markersize=4, color='m', label="point"))

    if raw:
        series.plot(label="raw", lw=lw, ax=ax)

    if ma:
        (series.rolling(ma).mean()
         .plot(ax=ax, label="{}{} ma".format(ma, time_bin), lw=lw))

    if ewma:
        if isinstance(ewma, int):
            (series.ewm(span=ewma).mean()
             .plot(ax=ax, label="emwa - span {}".format(ewma), lw=lw))
        else:
            (series.ewm(alpha=0.05).mean()
             .plot(ax=ax, label="emwa, $\alpha = 0.05$", lw=lw))

    if expanding:
        series.expanding().mean().plot(ax=ax, label="expanding_mean", lw=lw)

    if overall:
        (pd.DataFrame(series)
         .assign(global_mean=lambda x: x['count']
                 .mean())["global_mean"]
         .plot(ax=ax, label="global_mean", lw=lw))

    if median:
        (pd.DataFrame(series)
         .assign(global_median=lambda x: x['count'].median())["global_median"]
         .plot(ax=ax, label="global_median"))

    plt.tight_layout()
    plt.xlabel("datetime")

    if custom_yaxis is not None:
        def log_axis(x, pos):
            'The two args are the value and tick position'
            str_ = '$' + "2^{" + str(x) + "}" + '$'
            return str_
        formatter = FuncFormatter(log_axis)
        ax.yaxis.set_major_formatter(formatter)

    if title:
        ax.set_title(title)
    if custom_ax is not None:
        return
    else:
        return ax


TWEET_TOKENIZER = TweetTokenizer(preserve_case=False,
                                 strip_handles=True, reduce_len=False)
STOPWORDS = (set(nltk.corpus.stopwords.words("english")) |
             {"...", '…', '•', '’', "com"} |
             set(punctuation))


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def replace_urls(string, replacement=None):
    """
    Replace URLs in `string` with text of `replacement`
    """
    if replacement is None:
        replacement = "<-URL->"
    pattern = re.compile('(https?://)?(\w*[.]\w+)+([/?=&]+\w+)*')
    return re.sub(pattern, replacement, string)


def tokenizer(tweet_text, custom_words=None):
    text = (replace_urls(tweet_text))
    tokens = TWEET_TOKENIZER.tokenize(text)
    tokens = (token for token in tokens if token not in punctuation)
    tokens = (token for token in tokens if token not in STOPWORDS)
    tokens = (token for token in tokens if len(token) >= 3)
    if custom_words:
        tokens = (token for token in tokens if token not in custom_words)
    return list(tokens)


def get_frequent_terms(text_series, stop_words=None, ngram_range=None):
    if ngram_range is None:
        ngram_range = (1, 3)

    count_vectorizer = CountVectorizer(analyzer="word",
                                       tokenizer=tokenizer,
                                       stop_words=stop_words,
                                       ngram_range=ngram_range)

    term_freq_matrix = count_vectorizer.fit_transform(text_series)
    terms = count_vectorizer.get_feature_names()
    term_frequencies = term_freq_matrix.sum(axis=0).tolist()[0]

    term_freq_df = (pd.DataFrame(list(zip(terms, term_frequencies)),
                                 columns=["token", "count"])
                    .set_index("token")
                    .sort_values("count", ascending=False))
    return term_freq_df


def common_words_and_phrases(tweets, _stopwords=None, most_common=50,
                             ngram_range=None):
    if _stopwords is None:
        _stopwords = STOPWORDS
    tweet_texts = (t.all_text for t in tweets)
    return (get_frequent_terms(tweet_texts,
                               stop_words=_stopwords,
                               ngram_range=ngram_range)
            .head(most_common))


def summarize_tweet_text(tweets, samples=5):
    freq_terms = (get_frequent_terms(map(lambda x: x.all_text, tweets),
                  ngram_range=(2, 3))
                  .head(50))
    terms = list(freq_terms.reset_index()["token"])

    # print a few tweets
    # print("###########################################################")
    print("-----------------start summary-----------------------------")
    print("\t----sample tweets ----")
    _tweets = [t for t in it.islice(sorted(tweets,
                                           key=lambda x: x.favorite_count,
                                           reverse=True),
                                    samples)]
    for tweet in _tweets:
        print(f"tweet text:\n \t {tweet.all_text} \n favs: \t {tweet.favorite_count}")
        print()

    print("\t----sample terms ----")
    print(', '.join(terms))
    print("----------------- end summary------------------------------")
    # print("###########################################################")


def make_normalplot(df, random=True):
    if random:
        plt.plot(df.index.values,
                 np.random.normal(size=df.shape[0]),
                 lw=0.8,
                 alpha=0.75)
        plt.ylim((-5, 5))
        plt.title("Generated normal time series with $\sigma$ bands")
    else:
        plt.plot(df.index.values, df.values, lw=0.8, alpha=0.75)
        plt.ylim((-5, 8))
        plt.title("Dataframe with bands showing up to 3 sigma")

    plt.axhline(y=1, color="red")
    plt.axhline(y=-1, color="red")
    plt.axhline(y=2, color="orange")
    plt.axhline(y=-2, color="orange")
    plt.axhline(y=3, color="yellow")
    plt.axhline(y=-3, color="yellow")

    arrowprops = dict(arrowstyle="-",
                      color="black",
                      lw=2)

    #textprops = dict(rotation="vertical", fontsize=16)
    textprops = dict()

    plt.annotate("1 $\sigma$",
                 xy=(df.index.values[10], 1),
                 xytext=(df.index.values[10], -1.5),
                 arrowprops=arrowprops,
                 **textprops)

    plt.annotate("2 $\sigma$",
                 xy=(df.index.values[750], 2),
                 xytext=(df.index.values[750], -2.5),
                 arrowprops=arrowprops,
                 **textprops
                 )

    plt.annotate("3 $\sigma$",
                 xy=(df.index.values[1500], 3),
                 xytext=(df.index.values[1500], -3.5),
                 arrowprops=arrowprops,
                 **textprops
                 )


pop_star_rules = [{"artist": "katy_perry",
                   "rule": '("katy perry" OR @katyperry) -is:retweet lang:en'},
                  {"artist": "rihanna",
                   "rule": '(rihanna OR @rihanna) -is:retweet lang:en'},
                  {"artist":"lady_gaga",
                   "rule": '("lady gaga" OR @ladygaga) -is:retweet lang:en'},
                  {"artist": "ariana_grande",
                   "rule": '("ariana grande" OR @arianagrande) -is:retweet lang:en'},
                  {"artist": 'beyonce',
                   "rule": "(beyonce OR @beyonce) -is:retweet lang:en"},
                  {"artist": "selena_gomez",
                   "rule": '("selena gomez" OR @selenagomez) -is:retweet lang:en'}]


spotify_popular_artists_rule = """
(
"Drake" OR @Drake OR
"Ed Sheeran" OR @edsheeran OR
"The Chainsmokers" OR @TheChainsmokers OR
"The Weeknd" OR @theweeknd OR
"Justin Bieber" OR @justinbieber OR
"Calvin Harris" OR @CalvinHarris OR
"Major Lazer" OR @MAJORLAZER OR
"Shawn Mendes" OR @ShawnMendes OR
"Kygo" OR @KygoMusic OR
"Sia" OR @Sia OR
"Maroon 5" OR @maroon5 OR
"Imagine Dragons" OR @Imaginedragons OR
"Twenty One Pilots" OR @twentyonepilots OR
"Kendrick Lamar" OR @kendricklamar OR
"Rihanna" OR @rihanna OR
"David Guetta" OR @davidguetta OR
"Sam Smith" OR @samsmithworld OR
"Luis Fonsi" OR @LuisFonsi OR
"Charlie Puth" OR @charlieputh OR
"Clean Bandit" OR @cleanbandit OR
"Coldplay" OR @coldplay OR
"Jason Derulo" OR @jasonderulo OR
"Post Malone" OR @PostMalone OR
"ZAYN" OR @zaynmalik OR
"Avicii" OR @Avicii OR
"DJ Snake" OR @djsnake OR
"J Balvin" OR @JBALVIN OR
"Jonas Blue" OR @JonasBlue OR
"Adele" OR @Adele OR
"Martin Garrix" OR @MartinGarrix OR
"Bruno Mars" OR @BrunoMars OR
"Zara Larsson" OR @zaralarsson OR
"Fifth Harmony" OR @FifthHarmony OR
"DJ Khaled" OR @djkhaled OR
"Future" OR @1future OR
"Katy Perry" OR @katyperry OR
"Hailee Steinfeld" OR @HaileeSteinfeld OR
"One Direction" OR @onedirection OR
"Alan Walker" OR @IAmAlanWalker OR
"Robin Schulz" OR @robin_schulz OR
"Fetty Wap" OR @fettywap OR
"Alessia Cara" OR @alessiacara OR
"Ellie Goulding" OR @elliegoulding OR
"Cheat Codes" OR @CheatCodesMusic OR
"Mike Posner" OR @MikePosner OR
"Pitbull" OR @pitbull OR
"Meghan Trainor" OR @Meghan_Trainor
)
-is:retweet
lang:en
"""


spotify_charts_rule = """
(
"Post Malone" OR @PostMalone OR
"Lil Pump" OR @lilpump OR
"Camila Cabello" OR @Camila_Cabello OR
"Offset" OR @OffsetYRN OR
"G-Eazy" OR @G_Eazy OR
"A$AP Ferg" OR @burdxkeyz OR
"21 Savage" OR @21savage OR
"Sam Smith" OR @samsmithworld OR
"Migos" OR @Migos OR
"Ed Sheeran" OR @edsheeran OR
"Logic" OR @Logic301 OR
"Khalid" OR @thegreatkhalid OR
"Gucci Mane" OR @gucci1017 OR
"Maroon 5" OR @maroon5 OR
"Bebe Rexha" OR @BebeRexha OR
"Marshmello" OR @marshmellomusic OR
"Hailee Steinfeld" OR @HaileeSteinfeld OR
"Cardi B" OR @iamcardib OR
"Halsey" OR @halsey OR
"Kodak Black" OR @KodakBlack1k OR
"Kendrick Lamar" OR @kendricklamar OR
"Travis Scott" OR @trvisXX OR
"XXXTENTACION" OR @xxxtentacion OR
"French Montana" OR @FrencHMonTanA OR
"Demi Lovato" OR @ddlovato OR
"NAV" OR @beatsbynav OR
"Imagine Dragons" OR @Imaginedragons OR
"Charlie Puth" OR @charlieputh OR
"ZAYN" OR @zaynmalik OR
"Yo Gotti" OR @yogottikom OR
"YBN Nahmir" OR @nahmir205 OR
"Portugal. The Man" OR @portugaltheman OR
"Andy Williams" OR @ventriloquist29 OR
"Tay-K" OR @TAYK47USA OR
"Luis Fonsi" OR @LuisFonsi OR
"Clean Bandit" OR @cleanbandit OR
"Wham!" OR @13WHAM OR
"Playboi Carti" OR @damnbrandont OR
"Childish Gambino" OR @donaldglover OR
"SZA" OR @sza OR
"J Balvin" OR @JBALVIN OR
"Eminem" OR @Eminem OR
"Future" OR @1future OR
"2 Chainz" OR @2chainz OR
"Kesha" OR @KeshaRose OR
"Vince Guaraldi Trio" OR @RefinedPirate OR
"Band Aid" OR @FirstAidKitBand
)
-is:retweet
lang:en
"""
