import pandas as pd

# 1. ĐỌC DỮ LIỆU MOVIES
# Lược đồ: MovieID, Title, Genres
movies_cols = ['MovieID', 'Title', 'Genres']
movies = pd.read_csv('movies.txt', sep=', ', header=None, names=movies_cols, engine='python')

# 2. ĐỌC DỮ LIỆU RATINGS VÀ NỐI CHÚNG LẠI
# Lược đồ: UserID, MovieID, Rating, Timestamp
ratings_cols = ['UserID', 'MovieID', 'Rating', 'Timestamp']
ratings1 = pd.read_csv('ratings_1.txt', sep=', ', header=None, names=ratings_cols, engine='python')
ratings2 = pd.read_csv('ratings_2.txt', sep=', ', header=None, names=ratings_cols, engine='python')

# Nối 2 bảng ratings lại với nhau (Union)
ratings = pd.concat([ratings1, ratings2], ignore_index=True)

# 3. ĐỌC DỮ LIỆU USERS
# Lược đồ: UserID, Gender, Age, Occupation, Zip-code
users_cols = ['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code']
users = pd.read_csv('users.txt', sep=', ', header=None, names=users_cols, engine='python')

# 4. GỘP TOÀN BỘ DỮ LIỆU (JOIN)
# Gộp ratings với movies dựa trên MovieID, sau đó gộp tiếp với users dựa trên UserID
df_merged = ratings.merge(movies, on='MovieID', how='inner').merge(users, on='UserID', how='inner')

print("Gộp dữ liệu thành công! Tổng số dòng:", len(df_merged))
print(df_merged.head())

# ==========================================
# 5. MỘT SỐ CÂU TRUY VẤN MẪU THƯỜNG GẶP
# ==========================================

# Câu A: Tìm 10 bộ phim có điểm đánh giá trung bình cao nhất (chỉ xét phim có từ 5 lượt đánh giá trở lên)
movie_stats = df_merged.groupby('Title')['Rating'].agg(['count', 'mean'])
top_movies = movie_stats[movie_stats['count'] >= 5].sort_values(by='mean', ascending=False)
print("\n--- Top 10 phim rating cao nhất ---")
print(top_movies.head(10))

# Câu B: Thống kê số lượng đánh giá theo Giới tính (Gender)
gender_stats = df_merged.groupby('Gender')['Rating'].count()
print("\n--- Số lượng đánh giá theo giới tính ---")
print(gender_stats)