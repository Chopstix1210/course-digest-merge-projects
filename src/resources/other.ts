
import { visit } from '../utils/xml';
import * as Histogram from '../utils/histogram';
import { HasHistogram } from './common';

export interface OtherSummary extends HasHistogram {
  type: 'OtherSummary';
}

// Summarize an organization
export function summarize(file: string) : Promise<OtherSummary | string> {

  const summary : OtherSummary = {
    type: 'OtherSummary',
    elementHistogram: Histogram.create(),
  };

  return new Promise((resolve, reject) => {

    visit(file, (tag: string, attrs: Object) => {
      Histogram.update(summary.elementHistogram, tag, attrs);
    })
    .then((result) => {
      resolve(summary);
    })
    .catch(err => reject(err));
  });
}
