import React from 'react'
import Footer from '../components/Footer'

const About = () => {
    return (
        <>
            <div style={{ textAlign: "justify", padding: "40px", background: 'rgba(0,0,255,0.4)', margin: '0', fontFamily: "monospace" }}>
                <h2>What's Bible Challenge?</h2>
                <p>The goal is to build a solid reading habit. In a way that's attainable and realistic.</p>

                <h3>How do you do this?</h3>
                <p>Commit to studying your Bible topic for at least 30 minutes a day for 30 days, 60 days etc. Easy-peasy. To keep yopurself accountable, and use your community for support, you will journal your daily progress on the Whatsapp group.</p>

                <h3>Why does this work?</h3>
                <p>Studies have shown that for your brain to form and recognize new habits, repetition is key! Usually it takes anywhere from 21-30 days. Of course the more days the better :) Not only will the habit of studying get easier the deeper into your 30 days, 60 days etc. you get, you will also reap the rewards of how much progress you make. You can really get a lot done in 30 minutes a day for 30 days, 60 days etc.</p>
            </div>
            <Footer />
        </>
    )
}

export default About
