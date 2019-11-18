CREATE TABLE game(id integer not null  primary key AUTO_INCREMENT, 
		title varchar(100) not null 
			constraint "title length"
			check(length(title) <= 100),
		year_released integer not null 
				constraint "year_released validity"
                                 check(year_released+0=year_released
                                      and round(year_released)=year_released
                                      and year_released >= 1895
                                      and year_released <= 2050), 
		publisher varchar(30) 
				constraint "publisher length"
                                   check(coalesce(length(publisher),0)<=30),
				unique(title));
Create Table genre(id integer not null primary key, 
		genre varchar(100) not null 
			constraint "genre length"
			check(length(genre) <= 100),
			unique(genre));
create table game_genre(genre_id integer not null,
			game_id integer not null,
			foreign key(game_id) references game(id), 
			foreign key(genre_id) references genre(id)
			primary key(game_id, genre_id)
);
create table platform(id integer not null primary key AUTO_INCREMENT, 
			name varchar(30) not null 
				constraint "publisher length"
                                check(coalesce(length(name),0)<=30));
create table game_platform(game_id integer not null, 
				platform_id integer not null, 
			foreign key(game_id) references game(id),
			foreign key(platform_id) references platform(id) 
                                primary key(game_id, platform_id));

