import Home from './pages/home/Home';
import TopBar from './components/topbar/Topbar';
import Sidebar from './components/sidebar/Sidebar';

import './app.css';

function App() {
  return (
    <div>
      <TopBar />
      <div className="container">
        <Sidebar />
        <Home />
      </div>
    </div>
  );
}

export default App;
