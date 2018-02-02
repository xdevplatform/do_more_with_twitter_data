
Doing a thing With A Heading
============================

Hi, this is an example jupyter notebook.

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

Words and phrases

.. code:: ipython3

    df.query("item_name == 0")




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
          <th>SA0R</th>
          <td>Purchasing power of the consumer dollar</td>
          <td>0</td>
          <td>T</td>
          <td>398</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SAA</th>
          <td>Apparel</td>
          <td>0</td>
          <td>T</td>
          <td>187</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SAE</th>
          <td>Education and communication</td>
          <td>0</td>
          <td>T</td>
          <td>311</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SAF</th>
          <td>Food and beverages</td>
          <td>0</td>
          <td>T</td>
          <td>3</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SAG</th>
          <td>Other goods and services</td>
          <td>0</td>
          <td>T</td>
          <td>335</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SAH</th>
          <td>Housing</td>
          <td>0</td>
          <td>T</td>
          <td>136</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SAM</th>
          <td>Medical care</td>
          <td>0</td>
          <td>T</td>
          <td>250</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SAR</th>
          <td>Recreation</td>
          <td>0</td>
          <td>T</td>
          <td>269</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>SAT</th>
          <td>Transportation</td>
          <td>0</td>
          <td>T</td>
          <td>210</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



Subheading 3
^^^^^^^^^^^^

sub sub sub sub sub

.. math::  \forall x \in \mathbb{R} 

