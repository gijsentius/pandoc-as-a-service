import { MainState } from './state'
import { getStoreAccessors } from 'typesafe-vuex'
import { State } from '../state'
import { Flag } from '@/interfaces'

export const mutations = {
  addDocument(state: MainState, payload: File): void {
    state.document = payload
  },
  addFile(state: MainState, payload: File): void {
    state.files.push(payload)
  },
  addFlag(state: MainState, payload: Flag): void {
    state.flags.push(payload)
  },
  reset(state: MainState): void {
    state.document = undefined
    state.files = []
    state.flags = []
  }
}

const { commit } = getStoreAccessors<MainState | any, State>('')

export const commitAddFile = commit(mutations.addFile)
export const commitAddDocument = commit(mutations.addDocument)
export const commitAddFlag = commit(mutations.addFlag)
export const commitReset = commit(mutations.reset)
