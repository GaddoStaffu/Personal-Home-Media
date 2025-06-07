const api = 'http://192.168.1.57:8000';
let movieList = [];

fetch(`${api}/movie_list`)
  .then(response => response.json())
  .then(data => {
    movieList = data.movies;
    console.log('Movies loaded:', movieList);
    renderMovieList();
  })
  .catch(error => {
    console.error('Error fetching movie list:', error);
  });

function renderMovieList() {
  const movieListEl = document.getElementById('movieList');
  movieListEl.innerHTML = '';

  movieList.forEach(movie => {
    const li = document.createElement('li');
    li.textContent = movie;
    li.style.cursor = 'pointer';
    li.style.marginBottom = '8px';

    li.addEventListener('click', () => {
      playVideo(movie);
    });

    movieListEl.appendChild(li);
  });
}

function playVideo(movie) {
  const videoPlayer = document.getElementById('videoPlayer');
  const videoSource = document.getElementById('videoSource');

  videoSource.src = `${api}/media/${movie}`;  // Use api here instead of localhost
  videoPlayer.load();
  videoPlayer.play();
}
