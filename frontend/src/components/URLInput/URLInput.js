import React, { Component } from "react";
import cogoToast from 'cogo-toast';
import './URLInput.css';

function ShortenedUrl(props) {
  if (props.receivedShortenedUrl) {
    return (
      <div className="ShortenedUrl">
        <span className="OriginalUrl">
          Original URL: <a href={props.originalUrl}>{props.originalUrl}</a>
        </span>
        <span className="ShortUrl">
          Shortnd URL: <a href={props.shortenedUrl}>{props.shortenedUrl}</a>
        </span>
        {props.title !== '' &&
          <span className="UrlTitle">Title: {props.title}</span>
        }
      </div>
    )
  }
  return <></>;
}

class URLInput extends Component {
  constructor(props) {
    super(props);
    this.state = {
      url: '',
      originalUrl: '',
      receivedShortenedUrl: false,
      shortenedUrl: '',
      title: '',
    };

    this.handleUrlChange = this.handleUrlChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.validateUrl = this.validateUrl.bind(this);
    this.requestShorten = this.requestShorten.bind(this);
  }

  handleUrlChange(event) {
    this.setState({url: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    let url_valid = this.validateUrl(this.state.url);
    if (url_valid) {
      this.requestShorten();
    } else {
      cogoToast.error('Invalid URL');
    }
  }

  validateUrl(url) {
    let URL_PATTERN = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/;
    return URL_PATTERN.test(url);
  }

  requestShorten() {
    fetch('shorten/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({'url': this.state.url}),
    })
    .then((response) => response.json())
    .then((data) => {
      this.setState({
        receivedShortenedUrl: true,
        originalUrl: data.original_url,
        shortenedUrl: data.short_url,
        title: data.title !== null ? data.title : ''
      });
    })
    .catch((error) => {
      cogoToast.error(error);
    });
  }

  render() {
    return (
      <div className="URL">
        <form className="URLInput" onSubmit={this.handleSubmit}>
          <input className="Input" type="text" value={this.state.value} 
                onChange={this.handleUrlChange} placeholder="Enter URL">
          </input>
          <input className="SubmitButton" type="submit" value="Shorten" />
        </form>
        <ShortenedUrl className="ShortenedUrl"
                      receivedShortenedUrl={this.state.receivedShortenedUrl}
                      originalUrl={this.state.originalUrl}
                      shortenedUrl={this.state.shortenedUrl}
                      title={this.state.title} />
      </div>
    );
  }
}

export default URLInput;