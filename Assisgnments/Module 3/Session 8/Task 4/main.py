from insta_utils import like_count, comment_count

current_likes=227
current_comments=140

print(f"Your current likes:{current_likes}\nYour  current comments:{current_comments}")

current_likes =like_count(current_likes,int(input("Enter your new likes:")))
current_comments =comment_count(current_comments,int(input("Enter your new comments:")))

print(f"After update 1 -> Likes: {current_likes}, Comments: {current_comments}")

current_likes = like_count(current_likes, 25)
current_comments = comment_count(current_comments, 7)

print(f"After update 2 -> Likes: {current_likes}, Comments: {current_comments}")