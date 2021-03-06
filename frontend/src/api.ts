import axios from 'axios'
import { apiUrl } from './env'

export const api = {
  startConversion(document: File, other: File[]) {
    const formData = new FormData()
    formData.append('document', document)
    other.forEach(file => {
      formData.append('other', file)
    })
    axios.post(apiUrl + '/api/v1/convert', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'
      },
      responseType: 'blob'
    }).then((resp) => {
      const filename = document.name.split('.').slice(0, -1).join('.')
      downloadFile(resp.data, filename, 'application/pdf')
    })
  }
}

// Used from https://gist.github.com/davalapar/d0a5ba7cce4bc599f54800da22926da2
function downloadFile(data: any, filename: string, mime: string) {
  // It is necessary to create a new blob object with mime-type explicitly set
  // otherwise only Chrome works like it should
  const blob = new Blob([data], { type: mime || 'application/octet-stream' })
  if (typeof window.navigator.msSaveBlob !== 'undefined') {
    // IE doesn't allow using a blob object directly as link href.
    // Workaround for "HTML7007: One or more blob URLs were
    // revoked by closing the blob for which they were created.
    // These URLs will no longer resolve as the data backing
    // the URL has been freed."
    window.navigator.msSaveBlob(blob, filename)
    return
  }
  // Other browsers
  // Create a link pointing to the ObjectURL containing the blob
  const blobURL = window.URL.createObjectURL(blob)
  const tempLink = document.createElement('a')
  tempLink.style.display = 'none'
  tempLink.href = blobURL
  tempLink.setAttribute('download', filename)
  // Safari thinks _blank anchor are pop ups. We only want to set _blank
  // target if the browser does not support the HTML5 download attribute.
  // This allows you to download files in desktop safari if pop up blocking
  // is enabled.
  if (typeof tempLink.download === 'undefined') {
    tempLink.setAttribute('target', '_blank')
  }
  document.body.appendChild(tempLink)
  tempLink.click()
  document.body.removeChild(tempLink)
  setTimeout(() => {
    // For Firefox it is necessary to delay revoking the ObjectURL
    window.URL.revokeObjectURL(blobURL)
  }, 100)
}
