# -*- coding: utf-8 -*-

import os
os.chdir('/home/ankit/TechStack/FOTrend')

import config as config
import FeedlyClient.client as feedly



FEEDLY_REDIRECT_URI = "http://fabreadly.com/auth_callback"
FEEDLY_CLIENT_ID=config.client_id
FEEDLY_CLIENT_SECRET=config.client_secret
def get_feedly_client(token=None):
    if token:
        return FeedlyClient(token=token, sandbox=True)
    else:
        return FeedlyClient(
                            client_id=FEEDLY_CLIENT_ID, 
                            client_secret=FEEDLY_CLIENT_SECRET,
                            sandbox=True
        )
def auth(request):   
    feedly = get_feedly_client()
    # Redirect the user to the feedly authorization URL to get user code
    code_url = feedly.get_code_url(FEEDLY_REDIRECT_URI)    
    return redirect(code_url)
    
