"""
I will use Python as backend server language and Django web development framework.
For database, we can choose RDBMS DB like MySQL or NoSQL DB's like MongoDB or Cassandra.

## DATABASE Schema

    Tweet :
        tweet_id, user_id, tweet_text, time_posted
    User :
        user_id, first_name, last_name, dob, username


"""


## function to show tweets on the dashboard of a particular user

def tweet_list(request):
	tweets = Tweet.objects.all().filter(user_id=request.user.user_id)
	return render(request, 'blog/tweet_list.html', {'tweets': tweets})




## frontend code for the textbox where you can type your tweet and the
#   ubmit button that will send the request to publish this tweet

{% extends "tweets/tweet.html" %}
{% load crispy_forms_tags %}

{% block content%}
	<div class="content-section">
		<form action="" method="POST">
			{% csrf_token %}
			<fieldset class="form-group">
				<legend class="border-bottom mb-4">New tweet</legend>
				{{ form|crispy }}
			</fieldset>
			<div class="form-group">
				<button class="btn btn-outline-info" type="submit">Post</button>
			</div>
		</form>
		
	</div>
{% endblock content %}
