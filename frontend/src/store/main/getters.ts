import { MainState } from './state'
import { getStoreAccessors } from 'typesafe-vuex'
import { State } from '../state'

export const getters = {
  flags: (state: MainState) => {
    return (
      state.flags
    )
  },
  files: (state: MainState) => {
    return (state.files)
  },
  document: (state: MainState) => {
    return (state?.document)
  },
  documentPDFName: (state: MainState) => {
    if (state.document !== undefined) {
      return state.document.name.split('.').slice(0, -1).join('.')
    }
  }
}

const { read } = getStoreAccessors<MainState, State>('')

export const readFlags = read(getters.flags)
export const readFiles = read(getters.files)
export const readDocument = read(getters.document)
export const readDocumentPDFName = read(getters.documentPDFName)
