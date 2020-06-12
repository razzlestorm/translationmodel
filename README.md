# translationmodel
After cleaning a local dataset, this will (eventually) produce a model that can be used for NLP purposes, and translation of CN to EN

This model is built on roughly 10 years of translation assignments from one client, who does subtitles for CCTV. The relatively consistent 
formatting of the data makes it a bit easier to clean and work with.

After cleaning, an LSTM model was trained on the data (potentially with transfer learning?), and then tested on similar texts
to see if it could create something approaching human-level translation.
