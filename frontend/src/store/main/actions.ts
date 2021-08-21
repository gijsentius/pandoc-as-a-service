import { api } from '@/api'
import { getStoreAccessors } from 'typesafe-vuex'
import { ActionContext } from 'vuex'
import { State } from '../state'
import { MainState } from './state'
import {
  commitAddFlag,
  commitReset,
  commitAddFile,
  commitAddDocument
} from './mutations'
import { FileUpload, Flag } from '@/interfaces'

type MainContext = ActionContext<MainState, State>;

export const actions = {
  async convert(context: MainContext): Promise<void> {
    if (context.state.document !== undefined) {
      const response = (await Promise.all([
        api.startConversion(context.state.document, context.state.files),
        await new Promise<void>((resolve, reject) => setTimeout(() => resolve(), 500))
      ]))[0]
    }
  },
  addFlag(context: MainContext, payload: Flag): void {
    commitAddFlag(context, payload)
  },
  addFiles(context: MainContext, payload: File[]): void {
    payload.forEach(file => {
      commitAddFile(context, file)
    })
  },
  addDocument(context: MainContext, payload: File): void {
    commitAddDocument(context, payload)
  },
  reset(context: MainContext): void {
    commitReset(context)
  }
}

const { dispatch } = getStoreAccessors<MainState | any, State>('')

export const dispatchConvert = dispatch(actions.convert)
export const dispatchAddFlag = dispatch(actions.addFlag)
export const dispatchReset = dispatch(actions.reset)
export const dispatchAddFiles = dispatch(actions.addFiles)
export const dispatchAddDocument = dispatch(actions.addDocument)
