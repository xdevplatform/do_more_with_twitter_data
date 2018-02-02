
Doing a different thing With A Heading
======================================

Hi, this is an another example jupyter notebook.

.. code:: ipython3

    import os
    import pandas as pd

Subheading 1
------------

.. code:: ipython3

    df = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',
                     sep='\t')

.. code:: ipython3

    df.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>item_code</th>
          <th>item_name</th>
          <th>display_level</th>
          <th>selectable</th>
          <th>sort_sequence</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>AA0</th>
          <td>All items - old base</td>
          <td>0</td>
          <td>T</td>
          <td>2</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>AA0R</th>
          <td>Purchasing power of the consumer dollar - old ...</td>
          <td>0</td>
          <td>T</td>
          <td>399</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SA0</th>
          <td>All items</td>
          <td>0</td>
          <td>T</td>
          <td>1</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SA0E</th>
          <td>Energy</td>
          <td>1</td>
          <td>T</td>
          <td>374</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SA0L1</th>
          <td>All items less food</td>
          <td>1</td>
          <td>T</td>
          <td>358</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



Subheading 2
~~~~~~~~~~~~

some different words and phrases

Subheading 3
^^^^^^^^^^^^

more different words and phrases

.. code:: ipython3

    df.query("display_level == 'T'").head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>item_code</th>
          <th>item_name</th>
          <th>display_level</th>
          <th>selectable</th>
          <th>sort_sequence</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>AA0</th>
          <td>All items - old base</td>
          <td>0</td>
          <td>T</td>
          <td>2</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>AA0R</th>
          <td>Purchasing power of the consumer dollar - old ...</td>
          <td>0</td>
          <td>T</td>
          <td>399</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SA0</th>
          <td>All items</td>
          <td>0</td>
          <td>T</td>
          <td>1</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SA0E</th>
          <td>Energy</td>
          <td>1</td>
          <td>T</td>
          <td>374</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SA0L1</th>
          <td>All items less food</td>
          <td>1</td>
          <td>T</td>
          <td>358</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



h1 Heading 8-)
==============

h2 Heading
----------

h3 Heading
~~~~~~~~~~

h4 Heading
^^^^^^^^^^

h5 Heading
''''''''''

h6 Heading
          

Horizontal Rules
----------------

--------------

--------------

--------------

Typographic replacements
------------------------

Enable typographer option to see result.

(c) 

    (C) 

        (r) 

            (R) (tm) (TM) (p) (P) +-

test.. test... test..... test?..... test!....

!!!!!! ???? ,, -- ---

"Smartypants, double quotes" and 'single quotes'

Emphasis
--------

**This is bold text**

**This is bold text**

*This is italic text*

*This is italic text*

[STRIKEOUT:Strikethrough]

Blockquotes
-----------

