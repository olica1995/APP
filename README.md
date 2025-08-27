<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OLIX MEDIA APP</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<style>
/* ====== Base Styles ====== */
body { 
  margin:0; 
  font-family:'Roboto',sans-serif; 
  background:linear-gradient(100deg,#6a0dad,#ff00ff,#ff6600,#ffcc00);
  background-size:400% 400%;
  animation:gradientBG 15s ease infinite;
  color:#ffff; 
  display:flex; 
  flex-direction:column; 
  height:100vh; 
  overflow:hidden; 
}
@keyframes gradientBG {
  0% {background-position:0% 50%;}
  50% {background-position:100% 50%;}
  100% {background-position:0% 50%;}
}
body.dark-theme{background:linear-gradient(135deg,#211,#333);}
header{
  padding:20px;
  text-align:center;
  font-size:28px;
  font-weight:600;
  font-family:'Poppins',sans-serif;
  background:rgba(1,0,0,0.3);
  box-shadow:0 2px 6px rgba(0,0,0,0.4);
}
main{
  flex:1;
  display:flex;
  flex-direction:column;
  overflow:hidden;
}
#contentSection{
  flex:1;
  overflow-y:auto;
  padding:10px;
  padding-bottom:220px;
  background:rgba(0,0,0,0.2);
}
.tab-content{display:none; opacity:0; transform: translateY(10px); transition: opacity 0.3s, transform 0.3s;}
.tab-content.active{display:block; opacity:1; transform: translateY(0);}
.grid-container{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(120px,1fr));
  gap:12px;
}
.card{
  background-color: rgba(255,255,255,0.1);
  border-radius:10px;
  overflow:hidden;
  cursor:pointer;
  transition: transform 0.2s, box-shadow 0.2s, border 0.2s;
  text-align:center;
  padding-bottom:8px;
  border: 2px solid transparent;
  font-family:'Poppins',sans-serif;
}
.card.active{ border-color:#ffff; box-shadow: 0 0 20px rgba(255,255,255,0.5); animation: pulse 1.2s infinite; }
@keyframes pulse {
  0%,100% {transform: scale(1);}
  50% {transform: scale(1.05);}
}
.card:hover{ transform:scale(1.05); box-shadow:0 0 15px rgba(255,255,255,0.3); }
.card img{ width:100%; aspect-ratio:1/1; object-fit:cover; }
.card h3{ margin:8px 0 0 0; font-size:14px; }
#searchInput{
  width:100%; padding:10px; margin-bottom:10px;
  border-radius:12px; border:none; font-size:16px; outline:none;
  font-family:'Poppins',sans-serif;
}
.settings-item{
  margin:15px 0; display:flex; align-items:center; justify-content:space-between;
  font-family:'Poppins',sans-serif;
}
.settings-item label{font-size:18px;}
.toggle{
  width:50px; height:24px; background: linear-gradient(135deg, #aaa, #ddd); border-radius:12px;
  position:relative; cursor:pointer;
  transition: background 0.3s;
}
.toggle::after{
  content:''; position:absolute; top:2px; left:2px; width:20px; height:20px;
  background:#fff; border-radius:50%; transition:0.3s;
}
.toggle.active{ background-color:#ffccff; background: linear-gradient(135deg,#ff66ff,#ffccff); }
.toggle.active::after{ left:28px; }
nav.menu{
  display:flex; justify-content:space-around;
  background-color:rgba(0,0,0,0.3); padding:10px 0;
  position:fixed; bottom:0; width:100%; z-index:10;
  font-family:'Poppins',sans-serif;
}
.menu button{
  background:none; border:none; color:#fff; font-size:16px; cursor:pointer;
  display:flex; flex-direction:column; align-items:center; transition:color 0.2s;
}
.menu button.active{color:#ffccff;}
.icon{font-size:18px;margin-bottom:3px;} /* smaller icons */
#whatsappBtn {
  position:fixed; top:8px; right:8px;
  background:#25D366; color:#ffff; border-radius:50%;
  width:42px; height:42px; display:flex; justify-content:center; align-items:center;
  font-size:22px; cursor:pointer; box-shadow:0 4px 10px rgba(0,0,0,0.4);
  z-index:100; transition:transform 0.2s;
}
#whatsappBtn:hover { transform:scale(1.1); }

/* ================== YOUTUBE-LIKE PLAYER ================== */
#player {
  position: fixed;
  bottom: 64px;
  left: 50%;
  transform: translateX(-50%);
  width: 720px;
  max-width: 96%;
  aspect-ratio: 16/9;
  background: #000;
  border-radius: 12px;
  overflow: hidden;
  z-index: 20;
  display: flex;
  flex-direction: column;
  box-shadow: 0 8px 20px rgba(0,0,0,0.6);
  transition: all 0.35s ease-in-out;
  cursor: grab;
}
#player.mini {
  width: 240px; height: 135px; bottom: 80px; left: 20px;
  border-radius: 10px; transform: translateX(0);
  box-shadow: 0 4px 12px rgba(0,0,0,0.4);
  cursor: grab;
}
#player video, #player audio {
  width: 100%; height: 100%; border:none; outline:none;
  object-fit: cover; flex:1; background:#000;
}
#player img { width:100%; height:100%; object-fit:cover; display:block; z-index:0; }
#playerInfo { padding: 6px 12px; background: rgba(0,0,0,0.65);
  font-size: 15px; font-weight:500; font-family:'Poppins',sans-serif;
  color:#fff; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
#playerControls {
  position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%);
  z-index: 5; display: flex; gap: 8px; padding: 6px 10px;
  background: rgba(0,0,0,0.5); border-radius: 30px;
  backdrop-filter: blur(6px); opacity: 1; /* always visible */
}
  #playerControls.hidden {
  opacity: 0;
  pointer-events: none; /* prevents clicks when hidden */
  transition: opacity 0.3s ease;
}

.player-btn {
  background: rgba(255,255,255,0.15); border:none; color:#fff;
  border-radius: 50%; width:34px; height:34px;
  display:flex; align-items:center; justify-content:center;
  cursor:pointer; font-size:16px; transition: background 0.2s, transform 0.2s;
}
.player-btn:hover { background: rgba(255,255,255,0.3); transform: scale(1.1); }

/* Progress bar */
#playerProgress {
  position: absolute;
  bottom: 0; left: 0; width: 100%; height: 6px;
  background: rgba(255,255,255,0.2);
  cursor: pointer;
}
#playerProgress div {
  height: 100%;
  background: #ffccff;
  width: 4%;
  transition: width 0.2s;
}

/* Volume slider */
#volumeControl {
  width: 100px;
  height: 20px;
  background: rgba(255,255,255,0.2);
  border-radius: 3px;
  cursor: pointer;
  position: relative;
}
#volumeControl div {
  height: 100%;
  background: #ffccff;
  width: 100%;
  border-radius: 3px;
}

/* Mini Now Playing */
#miniNowPlaying {
  position:fixed; left:50px; bottom:60px; font-size:9px;
  background:rgba(0,0,0,0.65); padding:6px 12px; border-radius:24px;
  z-index:21; display:none; max-width:200px; white-space:nowrap;
  overflow:hidden; text-overflow:ellipsis; font-family:'Poppins',sans-serif;
  color:#fff; backdrop-filter:blur(6px); box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}

/* Loading Spinner */
#loadingSpinner {
  position:absolute; top:50%; left:50%;
  transform:translate(-50%,-50%);
  border:4px solid rgba(255,255,255,0.3);
  border-top:4px solid #fff;
  border-radius:50%; width:36px; height:36px;
  animation:spin 1s linear infinite;
  display:none; z-index:10;
}
@keyframes spin {100%{transform:translate(-50%,-50%) rotate(360deg);}}

@media(max-width:768px){
  #player { width:100%; left:0; transform:none; border-radius:0; }
}
@media(max-width:568px){
  .grid-container{ grid-template-columns:repeat(auto-fill,minmax(80px,1fr)); gap:6px; }
  .card h3{font-size:12px;}
  .icon{font-size:16px; margin-bottom:2px;}
}
</style>
</head>
<body>
<header>OLIX MEDIA APP</header>
<main>
  <div id="contentSection">
    <div class="tab-content" id="tvContent"></div>
    <div class="tab-content" id="radioContent"></div>
    <div class="tab-content" id="vodContent"></div>
    <div class="tab-content" id="searchContent">
      <input type="text" id="searchInput" placeholder="Search TV, Radio, VOD..." oninput="performSearch()">
      <div id="searchResults"></div>
    </div>
    <div class="tab-content" id="settingsContent">
      <div class="settings-item">
        <label>Dark Theme</label>
        <div class="toggle" id="themeToggle" onclick="toggleTheme()"></div>
      </div>
      <div class="settings-item">
        <label>Autoplay</label>
        <div class="toggle active" id="autoplayToggle" onclick="toggleAutoplay()"></div>
      </div>
    </div>
  </div>
</main>

<div id="player">
  <div id="loadingSpinner"></div>
  <img id="playerImage" src="" style="display:none;" alt="Now Playing">
  <div id="playerInfo"></div>
  <div id="playerProgress"><div></div></div>
  <div id="playerControls">
    <button class="player-btn" onclick="togglePlay()" aria-label="Play/Pause">⏯</button>
    <button class="player-btn" onclick="toggleMute()" aria-label="Mute/Unmute">🔊</button>
    <button class="player-btn" onclick="toggleFullscreen()" aria-label="Fullscreen">⛶</button>
    <button class="player-btn" onclick="expandPlayer()" aria-label="Expand">🔼</button>
    <button class="player-btn" onclick="minimizePlayer()" aria-label="Minimize">🔽</button>
    <div id="volumeControl"><div></div></div>
  </div>
</div>
<div id="miniNowPlaying"></div>

<a id="whatsappBtn" href="https://wa.me/256789223294" target="_blank" aria-label="Contact on WhatsApp">💬</a>

<nav class="menu">
  <button class="active" onclick="switchTab('tvContent', this)"><span class="icon">📺</span>TV</button>
  <button onclick="switchTab('radioContent', this)"><span class="icon">📻</span>Radio</button>
  <button onclick="switchTab('vodContent', this)"><span class="icon">🎬</span>VOD</button>
  <button onclick="switchTab('searchContent', this)"><span class="icon">🔍</span>Search</button>
  <button onclick="switchTab('settingsContent', this)"><span class="icon">⚙️</span>Settings</button>
</nav>

<script>
// =================== JS ===================
let autoplay = true;
let currentItem = null;
let player = document.getElementById('player');
let playerInfo = document.getElementById('playerInfo');
let miniNowPlaying = document.getElementById('miniNowPlaying');
let playerImage = document.getElementById('playerImage');
let mediaEl = null;
let spinner = document.getElementById('loadingSpinner');

const tabs = {
  tvContent:[
    {title:'News Channel', img:'https://via.placeholder.com/150x150?text=News', type:'hls', src:'https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8'},
    {title:'Sports Channel', img:'https://via.placeholder.com/150x150?text=Sports', type:'hls', src:'https://test-streams.mux.dev/test_001/stream.m3u8'}
  ],
  radioContent:[
    {title:'OLIX RADIO', img:'OLIX RADIO.png', type:'audio', src:'https://stream.zeno.fm/4mb1wxhrefhvv'},
    {title:'Unity FM 97.7', img:'KYOGA TV.jpg', type:'audio', src:'https://stream.zeno.fm/4mb1wxhrefhvv'},
    {title:'Pop Radio', img:'https://via.placeholder.com/150x150?text=Pop', type:'audio', src:'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'}
  ],
  vodContent:[
    {title:'Movie 1', img:'https://via.placeholder.com/150x150?text=Movie+1', type:'video', src:'https://www.w3schools.com/html/mov_bbb.mp4'}, 
    {title:'Kyoga TV Message', img:'KYOGA TV.jpg', type:'video', src:'omato angic.mp4'}
  ]
};

function renderTab(tabId){
  const container=document.getElementById(tabId);
  container.innerHTML='<div class="grid-container"></div>';
  const grid=container.querySelector('.grid-container');
  tabs[tabId].forEach(item=>{
    const card=document.createElement('div');
    card.classList.add('card');
    card.innerHTML=`<img src="${item.img}" alt="${item.title}"><h3>${item.title}</h3>`;
    card.onclick=()=>playItem(item, card, tabId);
    grid.appendChild(card);
  });
}
Object.keys(tabs).forEach(tabId=>renderTab(tabId));

function switchTab(tabId,btn){
  document.querySelectorAll('.tab-content').forEach(tc=>tc.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  document.querySelectorAll('.menu button').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
}

function createMedia(item){
  let el;
  if(item.type==='video'||item.type==='hls'){
    el=document.createElement('video');
    el.controls=false;
    el.autoplay=true;
    el.muted=false;
    el.playsInline=true;
    el.setAttribute("webkit-playsinline","true");
    el.setAttribute("controlsList","nodownload");
    el.style.background="#000";
    if(item.type==='hls' && Hls.isSupported()){
      const hls=new Hls();
      hls.loadSource(item.src);
      hls.attachMedia(el);
      hls.on(Hls.Events.MANIFEST_PARSED, () => { el.play().catch(()=>console.log("Autoplay blocked")); });
    }else{ el.src=item.src; el.play().catch(()=>console.log("Autoplay blocked")); }
    playerImage.style.display='none';
  } else if(item.type==='audio'){
    el=document.createElement('audio');
    el.controls=false;
    el.autoplay=true;
    el.src=item.src;
    el.style.width='100%';
    el.style.height='50px';
    playerImage.src=item.img;
    playerImage.style.display='block';
    el.play().catch(()=>console.log("Autoplay blocked"));
  }
  el.onwaiting = () => spinner.style.display = 'block';
  el.onplaying = () => spinner.style.display = 'none';
  el.onerror = () => { spinner.style.display = 'none'; playerInfo.innerText = "⚠️ Unable to load media"; };
  return el;
}

function playItem(item, card, tab){
  currentItem=item;
  document.querySelectorAll('.card').forEach(c=>c.classList.remove('active'));
  card.classList.add('active');
  if(mediaEl) player.removeChild(mediaEl);
  mediaEl=createMedia(item);
  player.insertBefore(mediaEl, playerInfo);
  playerInfo.innerText=item.title;
  expandPlayer();
}

function expandPlayer(){ player.classList.remove('mini'); miniNowPlaying.style.display='none'; }
function minimizePlayer(){ player.classList.add('mini'); if(currentItem) miniNowPlaying.innerText=currentItem.title; miniNowPlaying.style.display='block'; }
function toggleTheme(){ document.body.classList.toggle('dark-theme'); let active = document.body.classList.contains('dark-theme'); localStorage.setItem('theme', active); document.getElementById('themeToggle').classList.toggle('active', active); }
function toggleAutoplay(){ autoplay=!autoplay; localStorage.setItem('autoplay', autoplay); document.getElementById('autoplayToggle').classList.toggle('active', autoplay); }
function performSearch(){
  const query=document.getElementById('searchInput').value.toLowerCase();
  let results=[];
  Object.keys(tabs).forEach(tabId=>{ tabs[tabId].forEach(item=>{ if(item.title.toLowerCase().includes(query)) results.push({...item,tab:tabId}); }); });
  const container=document.getElementById('searchResults');
  container.innerHTML='';
  if(results.length>0){
    const grid=document.createElement('div'); grid.classList.add('grid-container');
    results.forEach(item=>{
      const card=document.createElement('div'); card.classList.add('card');
      let highlighted = item.title.replace(new RegExp(query, "gi"), match => `<mark>${match}</mark>`);
      card.innerHTML=`<img src="${item.img}" alt="${item.title}"><h3>${highlighted}</h3>`;
      card.onclick=()=>playItem(item, card, item.tab);
      grid.appendChild(card);
    });
    container.appendChild(grid);
  }else{ container.innerHTML='<p>No results found</p>'; }
}

function togglePlay(){ if(mediaEl){ if(mediaEl.paused){ mediaEl.play(); } else{ mediaEl.pause(); }} }
function toggleMute(){ if(mediaEl){ mediaEl.muted=!mediaEl.muted; } }
function toggleFullscreen(){
  if(player.requestFullscreen){ player.requestFullscreen(); }
  else if(player.webkitRequestFullscreen){ player.webkitRequestFullscreen(); }
  else if(player.msRequestFullscreen){ player.msRequestFullscreen(); }
}

// Progress bar
const progressBar = document.querySelector('#playerProgress div');
function updateProgress(){ if(mediaEl && mediaEl.duration){ const percent = (mediaEl.currentTime/mediaEl.duration)*100; progressBar.style.width = percent+'%'; } }
setInterval(updateProgress, 200);
document.getElementById('playerProgress').onclick = e => {
  if(mediaEl && mediaEl.duration){
    const rect = e.target.getBoundingClientRect();
    const x = e.clientX - rect.left;
    mediaEl.currentTime = (x/rect.width)*mediaEl.duration;
    updateProgress();
  }
};

// Volume control
const volumeBar = document.querySelector('#volumeControl div');
document.getElementById('volumeControl').onclick = e => {
  if(mediaEl){
    const rect = e.target.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const volume = Math.min(Math.max(x/rect.width,0),1);
    mediaEl.volume = volume;
    volumeBar.style.width = (volume*100)+'%';
  }
};

window.onload = () => {
  if(localStorage.getItem('theme') === 'true'){ document.body.classList.add('dark-theme'); document.getElementById('themeToggle').classList.add('active'); }
  autoplay = localStorage.getItem('autoplay') !== 'false';
  document.getElementById('autoplayToggle').classList.toggle('active', autoplay);
};

// Initialize first tab
switchTab('tvContent', document.querySelector('.menu button'));

// ================= DRAG MINI PLAYER =================
let isDragging = false;
let offset = {x:0,y:0};
player.addEventListener('mousedown', e=>{
  if(player.classList.contains('mini')){
    isDragging=true;
    offset.x=e.clientX-player.offsetLeft;
    offset.y=e.clientY-player.offsetTop;
    player.style.transition='none';
  }
});
document.addEventListener('mousemove', e=>{
  if(isDragging){ player.style.left=(e.clientX-offset.x)+'px'; player.style.top=(e.clientY-offset.y)+'px'; }
});
document.addEventListener('mouseup', e=>{
  if(isDragging){ isDragging=false; player.style.transition='all 0.3s ease'; }
});
  let controlsTimeout;

// Show controls and reset hide timer
function showControls() {
  const controls = document.getElementById('playerControls');
  controls.classList.remove('hidden');

  clearTimeout(controlsTimeout);
  controlsTimeout = setTimeout(() => {
    controls.classList.add('hidden');
  }, 5000); // hide after 5 seconds
}

// Track mouse movement over player to show controls
player.addEventListener('mousemove', showControls);
player.addEventListener('touchstart', showControls); // for mobile/touch

// Initially hide controls after 5 seconds
window.addEventListener('load', () => {
  controlsTimeout = setTimeout(() => {
    document.getElementById('playerControls').classList.add('hidden');
  }, 5000);
});

</script>
</body>
</html>
