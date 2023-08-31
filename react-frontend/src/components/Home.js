import React from 'react';
import Header from './Nav';
import UploadResume from '../components/UploadResume';
import JobRecommendations from '../components/JobRecommendations';

const Home = () => {
  const dummyRecommendations = []; // Replace with actual recommendations

  return (
    <div className="home">
      home
      <JobRecommendations recommendations={dummyRecommendations} />
    </div>
  );
};

export default Home;
